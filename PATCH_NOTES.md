# APEX Suite - Patch Notes

All notable changes to this project will be documented in this file, following Semantic Versioning (Major.Minor.Patch).

---

## [1.3.2] - Documentation & Final Polish - 2025-12-22
This is the final planned release for the v1 cycle, focusing on project documentation and final touches.
```diff
+ [DOCS] Created a professional `README.md` with complete installation, usage, and file structure information.
+ [DOCS] Added this dedicated `PATCH_NOTES.md` file to track the project's development history in detail.
# [UI] Minor adjustments to footer alignment and branding text.

[1.3.1] - User Interface Overhaul - 2025-12-10
Focused on creating a more professional and consistent user experience across the entire suite.
diff
# [UI] Standardized the layout of all tool headers and subheaders.
# [REFACTOR] Cleaned up and consolidated CSS rules to reduce redundancy.

[1.3.0] - Core Architectural Refactor - 2025-11-20
A major structural update to improve scalability, maintainability, and code quality. This was a significant background change that set the foundation for future development.
diff
+ [FEATURE] Implemented a modular, multi-page architecture.
# [REFACTOR] Migrated all individual tools (`analyzer_*`, `optimizer_*`) into a dedicated `utils/` directory.
# [REFACTOR] Rewrote the main script (`main.py`) to act as a router, dynamically importing and running tools as callable modules.
# [REFACTOR] Centralized Streamlit page configuration (`st.set_page_config`) into `main.py` to prevent errors and ensure consistency.
# [FIX] **CRITICAL:** Permanently resolved all `function 'run()' not found` errors by wrapping each tool's code in a standardized `run()` function.

[1.2.1] - Stability Patch - 2025-10-18
Post-release patch to address bugs found after the v1.2.0 launch.
diff
# [FIX] **Calculation Stability:** Corrected potential division-by-zero errors in all `analyzer` and `optimizer` tools. The app no longer crashes if inputs like 'Clicks', 'Conversions', or 'Ad Spend' are set to 0.
# [FIX] **BEP Accuracy:** Refined the Break-Even Point (BEP) calculation logic in the `Business Analyzer` for greater accuracy, especially when dealing with low margins.

[1.2.0] - Feature: Creative Evaluation - 2025-09-28
This version introduced the final pillar of analysis: Evaluation.
diff
+ [FEATURE] **Content Ranker:** A powerful new tool was added to the 'Ads Evaluation' pillar. It allows users to input performance data for multiple ad creatives and automatically ranks them from most to least profitable.
# [UI] Implemented a new "winner card" and dynamic data editor (`st.data_editor`) for the Content Ranker.

[1.1.1] - Usability Patch - 2025-09-02
Minor improvements based on early user feedback for the Optimizer tools.
diff
# [UI] Improved the clarity of the "Strategic Warning" text in both Optimizer tools to provide more actionable advice.
# [FIX] Corrected a minor formatting issue with currency display on the Optimizer dashboards.

[1.1.0] - Feature: Forecasting & Optimization - 2025-08-15
Expanded the suite's capabilities from simple analysis to proactive forecasting and planning.
diff
+ [FEATURE] **Product Optimizer:** Added to the 'Ads Forecasting' pillar. This tool helps users determine the ideal ad budget to achieve a specific net profit target for a single product.
+ [FEATURE] **Business Optimizer:** The second forecasting tool, designed for local businesses. It calculates the necessary ad budget to hit a target number of new customer visits.

[1.0.1] - Post-Launch Hotfix - 2025-07-25
A quick patch to address small issues found immediately after the initial launch.
# [FIX] Corrected a typo in the `ROI Analyzer` glossary.
# [FIX] Fixed a CSS alignment issue causing metric cards to misalign on certain screen sizes in the `Product Analyzer`.

[1.0.0] - Initial Release: The Analyzers - 2025-07-20
The official first launch of APEX Suite.
+ [LAUNCH] Initial public release of the APEX Suite project.
+ [FEATURE] **Product Analyzer v1.0:** The core tool for analyzing single-product campaign profitability.
+ [FEATURE] **Business Analyzer:** A tool for a holistic view of a business's monthly profit & loss.
+ [FEATURE] **ROI Analyzer:** A utility to compare the core efficiency of different marketing channels.
