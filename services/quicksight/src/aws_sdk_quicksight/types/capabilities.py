"""Generated from Smithy shape ``com.amazonaws.quicksight#Capabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.capability_state


class Capabilities(TypedDict, closed=True):
    export_to_csv: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to CSV files from the UI.</p>"""
    export_to_excel: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to Excel files from the UI.</p>"""
    export_to_pdf: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to PDF files from the UI.</p>"""
    print_reports: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to print reports.</p>"""
    create_and_update_themes: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to Create and Update themes.</p>"""
    add_or_run_anomaly_detection_for_analyses: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to add or run anomaly detection.</p>"""
    share_analyses: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share analyses.</p>"""
    create_and_update_datasets: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update datasets.</p>"""
    share_datasets: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share datasets.</p>"""
    subscribe_dashboard_email_reports: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to subscribe to email reports.</p>"""
    create_and_update_dashboard_email_reports: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update email reports.</p>"""
    share_dashboards: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share dashboards.</p>"""
    create_and_update_threshold_alerts: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update threshold alerts.</p>"""
    rename_shared_folders: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to rename shared folders.</p>"""
    create_shared_folders: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create shared folders.</p>"""
    create_and_update_data_sources: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update data sources.</p>"""
    share_data_sources: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share data sources.</p>"""
    view_account_spice_capacity: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to view account SPICE capacity.</p>"""
    create_spice_dataset: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create a SPICE dataset.</p>"""
    export_to_pdf_in_scheduled_reports: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to PDF files in scheduled email reports.</p>"""
    export_to_csv_in_scheduled_reports: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to CSV files in scheduled email reports.</p>"""
    export_to_excel_in_scheduled_reports: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to Excel files in scheduled email reports.</p>"""
    include_content_in_scheduled_reports_email: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to include content in scheduled email reports.</p>"""
    dashboard: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform dashboard-related actions.</p>"""
    analysis: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform analysis-related actions.</p>"""
    automate: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform automate-related actions.</p>"""
    flow: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform flow-related actions.</p>"""
    apps: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform apps-related actions.</p>"""
    create_and_update_apps: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create or update apps.</p>"""
    share_apps: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to share apps with other users.</p>"""
    invoke_apps_ai_inference: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to add and invoke AI inference in new and existing apps.</p>"""
    access_apps_native_data_store: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to access the native data store for new and existing apps.</p>"""
    publish_without_approval: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to enable approvals for flow share.</p>"""
    use_bedrock_models: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bedrock models for general knowledge step in flows.</p>"""
    perform_flow_ui_task: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use UI Agent step to perform tasks on public websites.</p>"""
    approve_flow_share_requests: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to review and approve sharing requests of Flows.</p>"""
    use_agent_web_search: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use internet to enhance results in Chat Agents, Flows, and Quick Research. Web search queries will be processed securely in an Amazon Web Services region <code>us-east-1</code>.</p>"""
    knowledge_base: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use knowledge bases to specify content from external applications.</p>"""
    action: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions in external services through Action connectors. Actions allow users to interact with third-party systems.</p>"""
    generic_http_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using REST API connection connectors.</p>"""
    create_and_update_generic_http_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update REST API connection actions.</p>"""
    share_generic_http_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share REST API connection actions.</p>"""
    use_generic_http_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use REST API connection actions.</p>"""
    asana_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Asana connectors.</p>"""
    create_and_update_asana_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Asana actions.</p>"""
    share_asana_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Asana actions.</p>"""
    use_asana_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Asana actions.</p>"""
    slack_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Slack connectors.</p>"""
    create_and_update_slack_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Slack actions.</p>"""
    share_slack_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Slack actions.</p>"""
    use_slack_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Slack actions.</p>"""
    service_now_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using ServiceNow connectors.</p>"""
    create_and_update_service_now_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update ServiceNow actions.</p>"""
    share_service_now_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share ServiceNow actions.</p>"""
    use_service_now_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use ServiceNow actions.</p>"""
    salesforce_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Salesforce connectors.</p>"""
    create_and_update_salesforce_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Salesforce actions.</p>"""
    share_salesforce_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Salesforce actions.</p>"""
    use_salesforce_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Salesforce actions.</p>"""
    ms_exchange_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft Outlook connectors.</p>"""
    create_and_update_ms_exchange_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft Outlook actions.</p>"""
    share_ms_exchange_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft Outlook actions.</p>"""
    use_ms_exchange_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft Outlook actions.</p>"""
    pager_duty_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using PagerDuty Advance connectors.</p>"""
    create_and_update_pager_duty_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update PagerDuty Advance actions.</p>"""
    share_pager_duty_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share PagerDuty Advance actions.</p>"""
    use_pager_duty_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use PagerDuty Advance actions.</p>"""
    jira_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Jira connectors.</p>"""
    create_and_update_jira_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Jira actions.</p>"""
    share_jira_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Jira actions.</p>"""
    use_jira_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Jira actions.</p>"""
    confluence_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Atlassian Confluence Cloud connectors.</p>"""
    create_and_update_confluence_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Atlassian Confluence Cloud actions.</p>"""
    share_confluence_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Atlassian Confluence Cloud actions.</p>"""
    use_confluence_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Atlassian Confluence Cloud actions.</p>"""
    one_drive_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft OneDrive connectors.</p>"""
    create_and_update_one_drive_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft OneDrive actions.</p>"""
    share_one_drive_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft OneDrive actions.</p>"""
    use_one_drive_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft OneDrive actions.</p>"""
    share_point_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft SharePoint Online connectors.</p>"""
    create_and_update_share_point_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft SharePoint Online actions.</p>"""
    share_share_point_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft SharePoint Online actions.</p>"""
    use_share_point_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft SharePoint Online actions.</p>"""
    ms_teams_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft Teams connectors.</p>"""
    create_and_update_ms_teams_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft Teams actions.</p>"""
    share_ms_teams_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft Teams actions.</p>"""
    use_ms_teams_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft Teams actions.</p>"""
    google_calendar_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Calendar connectors.</p>"""
    create_and_update_google_calendar_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Calendar actions.</p>"""
    share_google_calendar_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Calendar actions.</p>"""
    use_google_calendar_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Calendar actions.</p>"""
    zendesk_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Zendesk connectors.</p>"""
    create_and_update_zendesk_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Zendesk actions.</p>"""
    share_zendesk_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Zendesk actions.</p>"""
    use_zendesk_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Zendesk actions.</p>"""
    smartsheet_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Smartsheet connectors.</p>"""
    create_and_update_smartsheet_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Smartsheet actions.</p>"""
    share_smartsheet_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Smartsheet actions.</p>"""
    use_smartsheet_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Smartsheet actions.</p>"""
    sap_business_partner_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Business Partner connectors.</p>"""
    create_and_update_sap_business_partner_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Business Partner actions.</p>"""
    share_sap_business_partner_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Business Partner actions.</p>"""
    use_sap_business_partner_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Business Partner actions.</p>"""
    sap_product_master_data_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Product Master connectors.</p>"""
    create_and_update_sap_product_master_data_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Product Master actions.</p>"""
    share_sap_product_master_data_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Product Master actions.</p>"""
    use_sap_product_master_data_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Product Master actions.</p>"""
    sap_physical_inventory_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Physical Inventory connectors.</p>"""
    create_and_update_sap_physical_inventory_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Physical Inventory actions.</p>"""
    share_sap_physical_inventory_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Physical Inventory actions.</p>"""
    use_sap_physical_inventory_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Physical Inventory actions.</p>"""
    sap_bill_of_material_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Bill of Materials connectors.</p>"""
    create_and_update_sap_bill_of_material_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Bill of Materials actions.</p>"""
    share_sap_bill_of_material_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Bill of Materials actions.</p>"""
    use_sap_bill_of_material_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Bill of Materials actions.</p>"""
    sap_material_stock_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Material Stock connectors.</p>"""
    create_and_update_sap_material_stock_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Material Stock actions.</p>"""
    share_sap_material_stock_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Material Stock actions.</p>"""
    use_sap_material_stock_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Material Stock actions.</p>"""
    fact_set_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using FactSet connectors.</p>"""
    create_and_update_fact_set_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update FactSet actions.</p>"""
    share_fact_set_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share FactSet actions.</p>"""
    use_fact_set_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use FactSet actions.</p>"""
    amazon_s_three_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Amazon S3 connectors.</p>"""
    create_and_update_amazon_s_three_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Amazon S3 actions.</p>"""
    share_amazon_s_three_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Amazon S3 actions.</p>"""
    use_amazon_s_three_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Amazon S3 actions.</p>"""
    textract_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Textract connectors.</p>"""
    create_and_update_textract_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Textract actions.</p>"""
    share_textract_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Textract actions.</p>"""
    use_textract_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Textract actions.</p>"""
    comprehend_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Comprehend connectors.</p>"""
    create_and_update_comprehend_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Comprehend actions.</p>"""
    share_comprehend_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Comprehend actions.</p>"""
    use_comprehend_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Comprehend actions.</p>"""
    comprehend_medical_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Comprehend Medical connectors.</p>"""
    create_and_update_comprehend_medical_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Comprehend Medical actions.</p>"""
    share_comprehend_medical_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Comprehend Medical actions.</p>"""
    use_comprehend_medical_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Comprehend Medical actions.</p>"""
    amazon_bedrock_ars_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Bedrock Agent connectors.</p>"""
    create_and_update_amazon_bedrock_ars_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Bedrock Agent actions.</p>"""
    share_amazon_bedrock_ars_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Bedrock Agent actions.</p>"""
    use_amazon_bedrock_ars_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bedrock Agent actions.</p>"""
    amazon_bedrock_fs_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Bedrock Runtime connectors.</p>"""
    create_and_update_amazon_bedrock_fs_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Bedrock Runtime actions.</p>"""
    share_amazon_bedrock_fs_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Bedrock Runtime actions.</p>"""
    use_amazon_bedrock_fs_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bedrock Runtime actions.</p>"""
    amazon_bedrock_krs_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Bedrock Data Automation Runtime connectors.</p>"""
    create_and_update_amazon_bedrock_krs_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Bedrock Data Automation Runtime actions.</p>"""
    share_amazon_bedrock_krs_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Bedrock Data Automation Runtime actions.</p>"""
    use_amazon_bedrock_krs_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bedrock Data Automation Runtime actions.</p>"""
    mcp_action: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Model Context Protocol connectors.</p>"""
    create_and_update_mcp_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Model Context Protocol actions.</p>"""
    share_mcp_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Model Context Protocol actions.</p>"""
    use_mcp_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Model Context Protocol actions.</p>"""
    open_api_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using OpenAPI Specification connectors.</p>"""
    create_and_update_open_api_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update OpenAPI Specification actions.</p>"""
    share_open_api_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share OpenAPI Specification actions.</p>"""
    use_open_api_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use OpenAPI Specification actions.</p>"""
    sand_pgmi_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using S&P Global Market Intelligence connectors.</p>"""
    create_and_update_sand_pgmi_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update S&P Global Market Intelligence actions.</p>"""
    share_sand_pgmi_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share S&P Global Market Intelligence actions.</p>"""
    use_sand_pgmi_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use S&P Global Market Intelligence actions.</p>"""
    sand_p_global_energy_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using S&P Global Energy connectors.</p>"""
    create_and_update_sand_p_global_energy_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update S&P Global Energy actions.</p>"""
    share_sand_p_global_energy_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share S&P Global Energy actions.</p>"""
    use_sand_p_global_energy_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use S&P Global Energy actions.</p>"""
    bamboo_hr_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using BambooHR connectors.</p>"""
    create_and_update_bamboo_hr_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update BambooHR actions.</p>"""
    share_bamboo_hr_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share BambooHR actions.</p>"""
    use_bamboo_hr_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use BambooHR actions.</p>"""
    box_agent_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Box Agent connectors.</p>"""
    create_and_update_box_agent_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Box Agent actions.</p>"""
    share_box_agent_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Box Agent actions.</p>"""
    use_box_agent_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Box Agent actions.</p>"""
    canva_agent_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Canva Agent connectors.</p>"""
    create_and_update_canva_agent_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Canva Agent actions.</p>"""
    share_canva_agent_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Canva Agent actions.</p>"""
    use_canva_agent_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Canva Agent actions.</p>"""
    github_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using GitHub connectors.</p>"""
    create_and_update_github_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update GitHub actions.</p>"""
    share_github_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share GitHub actions.</p>"""
    use_github_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use GitHub actions.</p>"""
    notion_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Notion connectors.</p>"""
    create_and_update_notion_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Notion actions.</p>"""
    share_notion_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Notion actions.</p>"""
    use_notion_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Notion actions.</p>"""
    linear_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Linear connectors.</p>"""
    create_and_update_linear_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Linear actions.</p>"""
    share_linear_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Linear actions.</p>"""
    use_linear_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Linear actions.</p>"""
    hugging_face_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using HuggingFace connectors.</p>"""
    create_and_update_hugging_face_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update HuggingFace actions.</p>"""
    share_hugging_face_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share HuggingFace actions.</p>"""
    use_hugging_face_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use HuggingFace actions.</p>"""
    monday_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Monday connectors.</p>"""
    create_and_update_monday_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Monday actions.</p>"""
    share_monday_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Monday actions.</p>"""
    use_monday_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Monday actions.</p>"""
    hubspot_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Hubspot connectors.</p>"""
    create_and_update_hubspot_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Hubspot actions.</p>"""
    share_hubspot_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Hubspot actions.</p>"""
    use_hubspot_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Hubspot actions.</p>"""
    intercom_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Intercom connectors.</p>"""
    create_and_update_intercom_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Intercom actions.</p>"""
    share_intercom_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Intercom actions.</p>"""
    use_intercom_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Intercom actions.</p>"""
    new_relic_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using New Relic connectors.</p>"""
    create_and_update_new_relic_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update New Relic actions.</p>"""
    share_new_relic_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share New Relic actions.</p>"""
    use_new_relic_action: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use New Relic actions.</p>"""
    topic: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform Topic-related actions.</p>"""
    edit_visual_with_q: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to Edit Visual with AI</p>"""
    build_calculated_field_with_q: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to Build Calculation with AI</p>"""
    create_dashboard_executive_summary_with_q: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to Create Executive Summary</p>"""
    space: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform space-related actions.</p>"""
    create_spaces: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create spaces.</p>"""
    share_spaces: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share spaces with other users and groups.</p>"""
    chat_agent: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform chat-related actions.</p>"""
    create_chat_agents: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create chat agents.</p>"""
    share_chat_agents: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share chat agents with other users and groups.</p>"""
    research: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform research-related actions.</p>"""
    self_upgrade_user_role: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to enable users to upgrade their user role.</p>"""
    extension: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform Extension-related actions.</p>"""
    manage_shared_folders: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create, update, delete and view shared folders (both restricted and unrestricted), ability to add any asset to shared folders, and ability to share the folders.</p> <p> <b>Note:</b> This does <i>not</i> prevent inheriting access to assets that others share with them through folder membership.</p>"""
    generate_analyses: NotRequired[
        "aws_sdk_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to generate analysis using AI</p>"""
    story: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform Story-related actions.</p>"""
    scenario: NotRequired["aws_sdk_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform Scenario-related actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Capabilities) -> dict:
    out: dict = {}
    if "export_to_csv" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ExportToCsv"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["export_to_csv"]
        )
    if "export_to_excel" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ExportToExcel"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["export_to_excel"]
        )
    if "export_to_pdf" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ExportToPdf"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["export_to_pdf"]
        )
    if "print_reports" in value:
        import aws_sdk_quicksight.types.capability_state

        out["PrintReports"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["print_reports"]
        )
    if "create_and_update_themes" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateThemes"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_themes"]
            )
        )
    if "add_or_run_anomaly_detection_for_analyses" in value:
        import aws_sdk_quicksight.types.capability_state

        out["AddOrRunAnomalyDetectionForAnalyses"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["add_or_run_anomaly_detection_for_analyses"]
            )
        )
    if "share_analyses" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareAnalyses"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["share_analyses"]
        )
    if "create_and_update_datasets" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateDatasets"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_datasets"]
            )
        )
    if "share_datasets" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareDatasets"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["share_datasets"]
        )
    if "subscribe_dashboard_email_reports" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SubscribeDashboardEmailReports"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["subscribe_dashboard_email_reports"]
            )
        )
    if "create_and_update_dashboard_email_reports" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateDashboardEmailReports"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_dashboard_email_reports"]
            )
        )
    if "share_dashboards" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareDashboards"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_dashboards"]
            )
        )
    if "create_and_update_threshold_alerts" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateThresholdAlerts"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_threshold_alerts"]
            )
        )
    if "rename_shared_folders" in value:
        import aws_sdk_quicksight.types.capability_state

        out["RenameSharedFolders"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["rename_shared_folders"]
            )
        )
    if "create_shared_folders" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateSharedFolders"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_shared_folders"]
            )
        )
    if "create_and_update_data_sources" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateDataSources"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_data_sources"]
            )
        )
    if "share_data_sources" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareDataSources"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_data_sources"]
            )
        )
    if "view_account_spice_capacity" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ViewAccountSPICECapacity"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["view_account_spice_capacity"]
            )
        )
    if "create_spice_dataset" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateSPICEDataset"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_spice_dataset"]
            )
        )
    if "export_to_pdf_in_scheduled_reports" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ExportToPdfInScheduledReports"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["export_to_pdf_in_scheduled_reports"]
            )
        )
    if "export_to_csv_in_scheduled_reports" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ExportToCsvInScheduledReports"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["export_to_csv_in_scheduled_reports"]
            )
        )
    if "export_to_excel_in_scheduled_reports" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ExportToExcelInScheduledReports"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["export_to_excel_in_scheduled_reports"]
            )
        )
    if "include_content_in_scheduled_reports_email" in value:
        import aws_sdk_quicksight.types.capability_state

        out["IncludeContentInScheduledReportsEmail"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["include_content_in_scheduled_reports_email"]
            )
        )
    if "dashboard" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Dashboard"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["dashboard"]
        )
    if "analysis" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Analysis"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["analysis"]
        )
    if "automate" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Automate"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["automate"]
        )
    if "flow" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Flow"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["flow"]
        )
    if "apps" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Apps"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["apps"]
        )
    if "create_and_update_apps" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateApps"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_apps"]
            )
        )
    if "share_apps" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareApps"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["share_apps"]
        )
    if "invoke_apps_ai_inference" in value:
        import aws_sdk_quicksight.types.capability_state

        out["InvokeAppsAIInference"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["invoke_apps_ai_inference"]
            )
        )
    if "access_apps_native_data_store" in value:
        import aws_sdk_quicksight.types.capability_state

        out["AccessAppsNativeDataStore"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["access_apps_native_data_store"]
            )
        )
    if "publish_without_approval" in value:
        import aws_sdk_quicksight.types.capability_state

        out["PublishWithoutApproval"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["publish_without_approval"]
            )
        )
    if "use_bedrock_models" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseBedrockModels"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_bedrock_models"]
            )
        )
    if "perform_flow_ui_task" in value:
        import aws_sdk_quicksight.types.capability_state

        out["PerformFlowUiTask"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["perform_flow_ui_task"]
            )
        )
    if "approve_flow_share_requests" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ApproveFlowShareRequests"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["approve_flow_share_requests"]
            )
        )
    if "use_agent_web_search" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseAgentWebSearch"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_agent_web_search"]
            )
        )
    if "knowledge_base" in value:
        import aws_sdk_quicksight.types.capability_state

        out["KnowledgeBase"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["knowledge_base"]
        )
    if "action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Action"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["action"]
        )
    if "generic_http_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["GenericHTTPAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["generic_http_action"]
            )
        )
    if "create_and_update_generic_http_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateGenericHTTPAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_generic_http_action"]
            )
        )
    if "share_generic_http_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareGenericHTTPAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_generic_http_action"]
            )
        )
    if "use_generic_http_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseGenericHTTPAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_generic_http_action"]
            )
        )
    if "asana_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["AsanaAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["asana_action"]
        )
    if "create_and_update_asana_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateAsanaAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_asana_action"]
            )
        )
    if "share_asana_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareAsanaAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_asana_action"]
            )
        )
    if "use_asana_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseAsanaAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_asana_action"]
            )
        )
    if "slack_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SlackAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["slack_action"]
        )
    if "create_and_update_slack_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSlackAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_slack_action"]
            )
        )
    if "share_slack_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSlackAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_slack_action"]
            )
        )
    if "use_slack_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSlackAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_slack_action"]
            )
        )
    if "service_now_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ServiceNowAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["service_now_action"]
            )
        )
    if "create_and_update_service_now_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateServiceNowAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_service_now_action"]
            )
        )
    if "share_service_now_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareServiceNowAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_service_now_action"]
            )
        )
    if "use_service_now_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseServiceNowAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_service_now_action"]
            )
        )
    if "salesforce_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SalesforceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["salesforce_action"]
            )
        )
    if "create_and_update_salesforce_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSalesforceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_salesforce_action"]
            )
        )
    if "share_salesforce_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSalesforceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_salesforce_action"]
            )
        )
    if "use_salesforce_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSalesforceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_salesforce_action"]
            )
        )
    if "ms_exchange_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["MSExchangeAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["ms_exchange_action"]
            )
        )
    if "create_and_update_ms_exchange_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateMSExchangeAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_ms_exchange_action"]
            )
        )
    if "share_ms_exchange_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareMSExchangeAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_ms_exchange_action"]
            )
        )
    if "use_ms_exchange_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseMSExchangeAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_ms_exchange_action"]
            )
        )
    if "pager_duty_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["PagerDutyAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["pager_duty_action"]
            )
        )
    if "create_and_update_pager_duty_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdatePagerDutyAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_pager_duty_action"]
            )
        )
    if "share_pager_duty_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SharePagerDutyAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_pager_duty_action"]
            )
        )
    if "use_pager_duty_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UsePagerDutyAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_pager_duty_action"]
            )
        )
    if "jira_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["JiraAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["jira_action"]
        )
    if "create_and_update_jira_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateJiraAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_jira_action"]
            )
        )
    if "share_jira_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareJiraAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_jira_action"]
            )
        )
    if "use_jira_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseJiraAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["use_jira_action"]
        )
    if "confluence_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ConfluenceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["confluence_action"]
            )
        )
    if "create_and_update_confluence_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateConfluenceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_confluence_action"]
            )
        )
    if "share_confluence_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareConfluenceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_confluence_action"]
            )
        )
    if "use_confluence_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseConfluenceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_confluence_action"]
            )
        )
    if "one_drive_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["OneDriveAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["one_drive_action"]
            )
        )
    if "create_and_update_one_drive_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateOneDriveAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_one_drive_action"]
            )
        )
    if "share_one_drive_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareOneDriveAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_one_drive_action"]
            )
        )
    if "use_one_drive_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseOneDriveAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_one_drive_action"]
            )
        )
    if "share_point_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SharePointAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_point_action"]
            )
        )
    if "create_and_update_share_point_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSharePointAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_share_point_action"]
            )
        )
    if "share_share_point_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSharePointAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_share_point_action"]
            )
        )
    if "use_share_point_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSharePointAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_share_point_action"]
            )
        )
    if "ms_teams_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["MSTeamsAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["ms_teams_action"]
        )
    if "create_and_update_ms_teams_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateMSTeamsAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_ms_teams_action"]
            )
        )
    if "share_ms_teams_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareMSTeamsAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_ms_teams_action"]
            )
        )
    if "use_ms_teams_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseMSTeamsAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_ms_teams_action"]
            )
        )
    if "google_calendar_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["GoogleCalendarAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["google_calendar_action"]
            )
        )
    if "create_and_update_google_calendar_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateGoogleCalendarAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_calendar_action"]
            )
        )
    if "share_google_calendar_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareGoogleCalendarAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_google_calendar_action"]
            )
        )
    if "use_google_calendar_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseGoogleCalendarAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_google_calendar_action"]
            )
        )
    if "zendesk_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ZendeskAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["zendesk_action"]
        )
    if "create_and_update_zendesk_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateZendeskAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_zendesk_action"]
            )
        )
    if "share_zendesk_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareZendeskAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_zendesk_action"]
            )
        )
    if "use_zendesk_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseZendeskAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_zendesk_action"]
            )
        )
    if "smartsheet_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SmartsheetAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["smartsheet_action"]
            )
        )
    if "create_and_update_smartsheet_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSmartsheetAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_smartsheet_action"]
            )
        )
    if "share_smartsheet_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSmartsheetAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_smartsheet_action"]
            )
        )
    if "use_smartsheet_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSmartsheetAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_smartsheet_action"]
            )
        )
    if "sap_business_partner_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SAPBusinessPartnerAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["sap_business_partner_action"]
            )
        )
    if "create_and_update_sap_business_partner_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSAPBusinessPartnerAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_business_partner_action"]
            )
        )
    if "share_sap_business_partner_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSAPBusinessPartnerAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_sap_business_partner_action"]
            )
        )
    if "use_sap_business_partner_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSAPBusinessPartnerAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_sap_business_partner_action"]
            )
        )
    if "sap_product_master_data_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SAPProductMasterDataAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["sap_product_master_data_action"]
            )
        )
    if "create_and_update_sap_product_master_data_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSAPProductMasterDataAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_product_master_data_action"]
            )
        )
    if "share_sap_product_master_data_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSAPProductMasterDataAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_sap_product_master_data_action"]
            )
        )
    if "use_sap_product_master_data_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSAPProductMasterDataAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_sap_product_master_data_action"]
            )
        )
    if "sap_physical_inventory_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SAPPhysicalInventoryAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["sap_physical_inventory_action"]
            )
        )
    if "create_and_update_sap_physical_inventory_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSAPPhysicalInventoryAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_physical_inventory_action"]
            )
        )
    if "share_sap_physical_inventory_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSAPPhysicalInventoryAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_sap_physical_inventory_action"]
            )
        )
    if "use_sap_physical_inventory_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSAPPhysicalInventoryAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_sap_physical_inventory_action"]
            )
        )
    if "sap_bill_of_material_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SAPBillOfMaterialAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["sap_bill_of_material_action"]
            )
        )
    if "create_and_update_sap_bill_of_material_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSAPBillOfMaterialAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_bill_of_material_action"]
            )
        )
    if "share_sap_bill_of_material_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSAPBillOfMaterialAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_sap_bill_of_material_action"]
            )
        )
    if "use_sap_bill_of_material_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSAPBillOfMaterialAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_sap_bill_of_material_action"]
            )
        )
    if "sap_material_stock_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SAPMaterialStockAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["sap_material_stock_action"]
            )
        )
    if "create_and_update_sap_material_stock_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSAPMaterialStockAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_material_stock_action"]
            )
        )
    if "share_sap_material_stock_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSAPMaterialStockAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_sap_material_stock_action"]
            )
        )
    if "use_sap_material_stock_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSAPMaterialStockAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_sap_material_stock_action"]
            )
        )
    if "fact_set_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["FactSetAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["fact_set_action"]
        )
    if "create_and_update_fact_set_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateFactSetAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_fact_set_action"]
            )
        )
    if "share_fact_set_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareFactSetAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_fact_set_action"]
            )
        )
    if "use_fact_set_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseFactSetAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_fact_set_action"]
            )
        )
    if "amazon_s_three_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["AmazonSThreeAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["amazon_s_three_action"]
            )
        )
    if "create_and_update_amazon_s_three_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateAmazonSThreeAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_amazon_s_three_action"]
            )
        )
    if "share_amazon_s_three_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareAmazonSThreeAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_amazon_s_three_action"]
            )
        )
    if "use_amazon_s_three_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseAmazonSThreeAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_amazon_s_three_action"]
            )
        )
    if "textract_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["TextractAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["textract_action"]
            )
        )
    if "create_and_update_textract_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateTextractAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_textract_action"]
            )
        )
    if "share_textract_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareTextractAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_textract_action"]
            )
        )
    if "use_textract_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseTextractAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_textract_action"]
            )
        )
    if "comprehend_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ComprehendAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["comprehend_action"]
            )
        )
    if "create_and_update_comprehend_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateComprehendAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_comprehend_action"]
            )
        )
    if "share_comprehend_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareComprehendAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_comprehend_action"]
            )
        )
    if "use_comprehend_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseComprehendAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_comprehend_action"]
            )
        )
    if "comprehend_medical_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ComprehendMedicalAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["comprehend_medical_action"]
            )
        )
    if "create_and_update_comprehend_medical_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateComprehendMedicalAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_comprehend_medical_action"]
            )
        )
    if "share_comprehend_medical_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareComprehendMedicalAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_comprehend_medical_action"]
            )
        )
    if "use_comprehend_medical_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseComprehendMedicalAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_comprehend_medical_action"]
            )
        )
    if "amazon_bedrock_ars_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["AmazonBedrockARSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["amazon_bedrock_ars_action"]
            )
        )
    if "create_and_update_amazon_bedrock_ars_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateAmazonBedrockARSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_amazon_bedrock_ars_action"]
            )
        )
    if "share_amazon_bedrock_ars_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareAmazonBedrockARSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_amazon_bedrock_ars_action"]
            )
        )
    if "use_amazon_bedrock_ars_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseAmazonBedrockARSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_amazon_bedrock_ars_action"]
            )
        )
    if "amazon_bedrock_fs_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["AmazonBedrockFSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["amazon_bedrock_fs_action"]
            )
        )
    if "create_and_update_amazon_bedrock_fs_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateAmazonBedrockFSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_amazon_bedrock_fs_action"]
            )
        )
    if "share_amazon_bedrock_fs_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareAmazonBedrockFSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_amazon_bedrock_fs_action"]
            )
        )
    if "use_amazon_bedrock_fs_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseAmazonBedrockFSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_amazon_bedrock_fs_action"]
            )
        )
    if "amazon_bedrock_krs_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["AmazonBedrockKRSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["amazon_bedrock_krs_action"]
            )
        )
    if "create_and_update_amazon_bedrock_krs_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateAmazonBedrockKRSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_amazon_bedrock_krs_action"]
            )
        )
    if "share_amazon_bedrock_krs_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareAmazonBedrockKRSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_amazon_bedrock_krs_action"]
            )
        )
    if "use_amazon_bedrock_krs_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseAmazonBedrockKRSAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_amazon_bedrock_krs_action"]
            )
        )
    if "mcp_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["MCPAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["mcp_action"]
        )
    if "create_and_update_mcp_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateMCPAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_mcp_action"]
            )
        )
    if "share_mcp_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareMCPAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_mcp_action"]
            )
        )
    if "use_mcp_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseMCPAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["use_mcp_action"]
        )
    if "open_api_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["OpenAPIAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["open_api_action"]
        )
    if "create_and_update_open_api_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateOpenAPIAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_open_api_action"]
            )
        )
    if "share_open_api_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareOpenAPIAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_open_api_action"]
            )
        )
    if "use_open_api_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseOpenAPIAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_open_api_action"]
            )
        )
    if "sand_pgmi_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SandPGMIAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["sand_pgmi_action"]
            )
        )
    if "create_and_update_sand_pgmi_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSandPGMIAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sand_pgmi_action"]
            )
        )
    if "share_sand_pgmi_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSandPGMIAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_sand_pgmi_action"]
            )
        )
    if "use_sand_pgmi_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSandPGMIAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_sand_pgmi_action"]
            )
        )
    if "sand_p_global_energy_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SandPGlobalEnergyAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["sand_p_global_energy_action"]
            )
        )
    if "create_and_update_sand_p_global_energy_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateSandPGlobalEnergyAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sand_p_global_energy_action"]
            )
        )
    if "share_sand_p_global_energy_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSandPGlobalEnergyAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_sand_p_global_energy_action"]
            )
        )
    if "use_sand_p_global_energy_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseSandPGlobalEnergyAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_sand_p_global_energy_action"]
            )
        )
    if "bamboo_hr_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["BambooHRAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["bamboo_hr_action"]
            )
        )
    if "create_and_update_bamboo_hr_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateBambooHRAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_bamboo_hr_action"]
            )
        )
    if "share_bamboo_hr_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareBambooHRAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_bamboo_hr_action"]
            )
        )
    if "use_bamboo_hr_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseBambooHRAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_bamboo_hr_action"]
            )
        )
    if "box_agent_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["BoxAgentAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["box_agent_action"]
            )
        )
    if "create_and_update_box_agent_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateBoxAgentAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_box_agent_action"]
            )
        )
    if "share_box_agent_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareBoxAgentAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_box_agent_action"]
            )
        )
    if "use_box_agent_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseBoxAgentAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_box_agent_action"]
            )
        )
    if "canva_agent_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CanvaAgentAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["canva_agent_action"]
            )
        )
    if "create_and_update_canva_agent_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateCanvaAgentAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_canva_agent_action"]
            )
        )
    if "share_canva_agent_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareCanvaAgentAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_canva_agent_action"]
            )
        )
    if "use_canva_agent_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseCanvaAgentAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_canva_agent_action"]
            )
        )
    if "github_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["GithubAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["github_action"]
        )
    if "create_and_update_github_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateGithubAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_github_action"]
            )
        )
    if "share_github_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareGithubAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_github_action"]
            )
        )
    if "use_github_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseGithubAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_github_action"]
            )
        )
    if "notion_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["NotionAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["notion_action"]
        )
    if "create_and_update_notion_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateNotionAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_notion_action"]
            )
        )
    if "share_notion_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareNotionAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_notion_action"]
            )
        )
    if "use_notion_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseNotionAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_notion_action"]
            )
        )
    if "linear_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["LinearAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["linear_action"]
        )
    if "create_and_update_linear_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateLinearAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_linear_action"]
            )
        )
    if "share_linear_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareLinearAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_linear_action"]
            )
        )
    if "use_linear_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseLinearAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_linear_action"]
            )
        )
    if "hugging_face_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["HuggingFaceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["hugging_face_action"]
            )
        )
    if "create_and_update_hugging_face_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateHuggingFaceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_hugging_face_action"]
            )
        )
    if "share_hugging_face_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareHuggingFaceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_hugging_face_action"]
            )
        )
    if "use_hugging_face_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseHuggingFaceAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_hugging_face_action"]
            )
        )
    if "monday_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["MondayAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["monday_action"]
        )
    if "create_and_update_monday_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateMondayAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_monday_action"]
            )
        )
    if "share_monday_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareMondayAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_monday_action"]
            )
        )
    if "use_monday_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseMondayAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_monday_action"]
            )
        )
    if "hubspot_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["HubspotAction"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["hubspot_action"]
        )
    if "create_and_update_hubspot_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateHubspotAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_hubspot_action"]
            )
        )
    if "share_hubspot_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareHubspotAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_hubspot_action"]
            )
        )
    if "use_hubspot_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseHubspotAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_hubspot_action"]
            )
        )
    if "intercom_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["IntercomAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["intercom_action"]
            )
        )
    if "create_and_update_intercom_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateIntercomAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_intercom_action"]
            )
        )
    if "share_intercom_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareIntercomAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_intercom_action"]
            )
        )
    if "use_intercom_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseIntercomAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_intercom_action"]
            )
        )
    if "new_relic_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["NewRelicAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["new_relic_action"]
            )
        )
    if "create_and_update_new_relic_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateAndUpdateNewRelicAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_and_update_new_relic_action"]
            )
        )
    if "share_new_relic_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareNewRelicAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_new_relic_action"]
            )
        )
    if "use_new_relic_action" in value:
        import aws_sdk_quicksight.types.capability_state

        out["UseNewRelicAction"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["use_new_relic_action"]
            )
        )
    if "topic" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Topic"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["topic"]
        )
    if "edit_visual_with_q" in value:
        import aws_sdk_quicksight.types.capability_state

        out["EditVisualWithQ"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["edit_visual_with_q"]
            )
        )
    if "build_calculated_field_with_q" in value:
        import aws_sdk_quicksight.types.capability_state

        out["BuildCalculatedFieldWithQ"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["build_calculated_field_with_q"]
            )
        )
    if "create_dashboard_executive_summary_with_q" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateDashboardExecutiveSummaryWithQ"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_dashboard_executive_summary_with_q"]
            )
        )
    if "space" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Space"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["space"]
        )
    if "create_spaces" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateSpaces"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["create_spaces"]
        )
    if "share_spaces" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareSpaces"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["share_spaces"]
        )
    if "chat_agent" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ChatAgent"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["chat_agent"]
        )
    if "create_chat_agents" in value:
        import aws_sdk_quicksight.types.capability_state

        out["CreateChatAgents"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["create_chat_agents"]
            )
        )
    if "share_chat_agents" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ShareChatAgents"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["share_chat_agents"]
            )
        )
    if "research" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Research"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["research"]
        )
    if "self_upgrade_user_role" in value:
        import aws_sdk_quicksight.types.capability_state

        out["SelfUpgradeUserRole"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["self_upgrade_user_role"]
            )
        )
    if "extension" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Extension"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["extension"]
        )
    if "manage_shared_folders" in value:
        import aws_sdk_quicksight.types.capability_state

        out["ManageSharedFolders"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["manage_shared_folders"]
            )
        )
    if "generate_analyses" in value:
        import aws_sdk_quicksight.types.capability_state

        out["GenerateAnalyses"] = (
            aws_sdk_quicksight.types.capability_state.serialize_json(
                value["generate_analyses"]
            )
        )
    if "story" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Story"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["story"]
        )
    if "scenario" in value:
        import aws_sdk_quicksight.types.capability_state

        out["Scenario"] = aws_sdk_quicksight.types.capability_state.serialize_json(
            value["scenario"]
        )
    return out


def deserialize_json(data: dict) -> Capabilities:
    out: Capabilities = {}  # type: ignore[typeddict-item]
    if "ExportToCsv" in data:
        import aws_sdk_quicksight.types.capability_state

        out["export_to_csv"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ExportToCsv"]
            )
        )
    if "ExportToExcel" in data:
        import aws_sdk_quicksight.types.capability_state

        out["export_to_excel"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ExportToExcel"]
            )
        )
    if "ExportToPdf" in data:
        import aws_sdk_quicksight.types.capability_state

        out["export_to_pdf"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ExportToPdf"]
            )
        )
    if "PrintReports" in data:
        import aws_sdk_quicksight.types.capability_state

        out["print_reports"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["PrintReports"]
            )
        )
    if "CreateAndUpdateThemes" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_themes"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateThemes"]
            )
        )
    if "AddOrRunAnomalyDetectionForAnalyses" in data:
        import aws_sdk_quicksight.types.capability_state

        out["add_or_run_anomaly_detection_for_analyses"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["AddOrRunAnomalyDetectionForAnalyses"]
            )
        )
    if "ShareAnalyses" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_analyses"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareAnalyses"]
            )
        )
    if "CreateAndUpdateDatasets" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_datasets"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateDatasets"]
            )
        )
    if "ShareDatasets" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_datasets"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareDatasets"]
            )
        )
    if "SubscribeDashboardEmailReports" in data:
        import aws_sdk_quicksight.types.capability_state

        out["subscribe_dashboard_email_reports"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SubscribeDashboardEmailReports"]
            )
        )
    if "CreateAndUpdateDashboardEmailReports" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_dashboard_email_reports"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateDashboardEmailReports"]
            )
        )
    if "ShareDashboards" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_dashboards"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareDashboards"]
            )
        )
    if "CreateAndUpdateThresholdAlerts" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_threshold_alerts"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateThresholdAlerts"]
            )
        )
    if "RenameSharedFolders" in data:
        import aws_sdk_quicksight.types.capability_state

        out["rename_shared_folders"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["RenameSharedFolders"]
            )
        )
    if "CreateSharedFolders" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_shared_folders"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateSharedFolders"]
            )
        )
    if "CreateAndUpdateDataSources" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_data_sources"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateDataSources"]
            )
        )
    if "ShareDataSources" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_data_sources"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareDataSources"]
            )
        )
    if "ViewAccountSPICECapacity" in data:
        import aws_sdk_quicksight.types.capability_state

        out["view_account_spice_capacity"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ViewAccountSPICECapacity"]
            )
        )
    if "CreateSPICEDataset" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_spice_dataset"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateSPICEDataset"]
            )
        )
    if "ExportToPdfInScheduledReports" in data:
        import aws_sdk_quicksight.types.capability_state

        out["export_to_pdf_in_scheduled_reports"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ExportToPdfInScheduledReports"]
            )
        )
    if "ExportToCsvInScheduledReports" in data:
        import aws_sdk_quicksight.types.capability_state

        out["export_to_csv_in_scheduled_reports"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ExportToCsvInScheduledReports"]
            )
        )
    if "ExportToExcelInScheduledReports" in data:
        import aws_sdk_quicksight.types.capability_state

        out["export_to_excel_in_scheduled_reports"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ExportToExcelInScheduledReports"]
            )
        )
    if "IncludeContentInScheduledReportsEmail" in data:
        import aws_sdk_quicksight.types.capability_state

        out["include_content_in_scheduled_reports_email"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["IncludeContentInScheduledReportsEmail"]
            )
        )
    if "Dashboard" in data:
        import aws_sdk_quicksight.types.capability_state

        out["dashboard"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Dashboard"]
        )
    if "Analysis" in data:
        import aws_sdk_quicksight.types.capability_state

        out["analysis"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Analysis"]
        )
    if "Automate" in data:
        import aws_sdk_quicksight.types.capability_state

        out["automate"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Automate"]
        )
    if "Flow" in data:
        import aws_sdk_quicksight.types.capability_state

        out["flow"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Flow"]
        )
    if "Apps" in data:
        import aws_sdk_quicksight.types.capability_state

        out["apps"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Apps"]
        )
    if "CreateAndUpdateApps" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_apps"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateApps"]
            )
        )
    if "ShareApps" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_apps"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["ShareApps"]
        )
    if "InvokeAppsAIInference" in data:
        import aws_sdk_quicksight.types.capability_state

        out["invoke_apps_ai_inference"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["InvokeAppsAIInference"]
            )
        )
    if "AccessAppsNativeDataStore" in data:
        import aws_sdk_quicksight.types.capability_state

        out["access_apps_native_data_store"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["AccessAppsNativeDataStore"]
            )
        )
    if "PublishWithoutApproval" in data:
        import aws_sdk_quicksight.types.capability_state

        out["publish_without_approval"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["PublishWithoutApproval"]
            )
        )
    if "UseBedrockModels" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_bedrock_models"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseBedrockModels"]
            )
        )
    if "PerformFlowUiTask" in data:
        import aws_sdk_quicksight.types.capability_state

        out["perform_flow_ui_task"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["PerformFlowUiTask"]
            )
        )
    if "ApproveFlowShareRequests" in data:
        import aws_sdk_quicksight.types.capability_state

        out["approve_flow_share_requests"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ApproveFlowShareRequests"]
            )
        )
    if "UseAgentWebSearch" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_agent_web_search"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseAgentWebSearch"]
            )
        )
    if "KnowledgeBase" in data:
        import aws_sdk_quicksight.types.capability_state

        out["knowledge_base"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["KnowledgeBase"]
            )
        )
    if "Action" in data:
        import aws_sdk_quicksight.types.capability_state

        out["action"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Action"]
        )
    if "GenericHTTPAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["generic_http_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["GenericHTTPAction"]
            )
        )
    if "CreateAndUpdateGenericHTTPAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_generic_http_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGenericHTTPAction"]
            )
        )
    if "ShareGenericHTTPAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_generic_http_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareGenericHTTPAction"]
            )
        )
    if "UseGenericHTTPAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_generic_http_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseGenericHTTPAction"]
            )
        )
    if "AsanaAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["asana_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["AsanaAction"]
            )
        )
    if "CreateAndUpdateAsanaAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_asana_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAsanaAction"]
            )
        )
    if "ShareAsanaAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_asana_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareAsanaAction"]
            )
        )
    if "UseAsanaAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_asana_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseAsanaAction"]
            )
        )
    if "SlackAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["slack_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SlackAction"]
            )
        )
    if "CreateAndUpdateSlackAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_slack_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSlackAction"]
            )
        )
    if "ShareSlackAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_slack_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSlackAction"]
            )
        )
    if "UseSlackAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_slack_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSlackAction"]
            )
        )
    if "ServiceNowAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["service_now_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ServiceNowAction"]
            )
        )
    if "CreateAndUpdateServiceNowAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_service_now_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateServiceNowAction"]
            )
        )
    if "ShareServiceNowAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_service_now_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareServiceNowAction"]
            )
        )
    if "UseServiceNowAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_service_now_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseServiceNowAction"]
            )
        )
    if "SalesforceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["salesforce_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SalesforceAction"]
            )
        )
    if "CreateAndUpdateSalesforceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_salesforce_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSalesforceAction"]
            )
        )
    if "ShareSalesforceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_salesforce_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSalesforceAction"]
            )
        )
    if "UseSalesforceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_salesforce_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSalesforceAction"]
            )
        )
    if "MSExchangeAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["ms_exchange_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["MSExchangeAction"]
            )
        )
    if "CreateAndUpdateMSExchangeAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_ms_exchange_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMSExchangeAction"]
            )
        )
    if "ShareMSExchangeAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_ms_exchange_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareMSExchangeAction"]
            )
        )
    if "UseMSExchangeAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_ms_exchange_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseMSExchangeAction"]
            )
        )
    if "PagerDutyAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["pager_duty_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["PagerDutyAction"]
            )
        )
    if "CreateAndUpdatePagerDutyAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_pager_duty_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdatePagerDutyAction"]
            )
        )
    if "SharePagerDutyAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_pager_duty_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SharePagerDutyAction"]
            )
        )
    if "UsePagerDutyAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_pager_duty_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UsePagerDutyAction"]
            )
        )
    if "JiraAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["jira_action"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["JiraAction"]
        )
    if "CreateAndUpdateJiraAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_jira_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateJiraAction"]
            )
        )
    if "ShareJiraAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_jira_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareJiraAction"]
            )
        )
    if "UseJiraAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_jira_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseJiraAction"]
            )
        )
    if "ConfluenceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["confluence_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ConfluenceAction"]
            )
        )
    if "CreateAndUpdateConfluenceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_confluence_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateConfluenceAction"]
            )
        )
    if "ShareConfluenceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_confluence_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareConfluenceAction"]
            )
        )
    if "UseConfluenceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_confluence_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseConfluenceAction"]
            )
        )
    if "OneDriveAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["one_drive_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["OneDriveAction"]
            )
        )
    if "CreateAndUpdateOneDriveAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_one_drive_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateOneDriveAction"]
            )
        )
    if "ShareOneDriveAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_one_drive_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareOneDriveAction"]
            )
        )
    if "UseOneDriveAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_one_drive_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseOneDriveAction"]
            )
        )
    if "SharePointAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_point_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SharePointAction"]
            )
        )
    if "CreateAndUpdateSharePointAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_share_point_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSharePointAction"]
            )
        )
    if "ShareSharePointAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_share_point_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSharePointAction"]
            )
        )
    if "UseSharePointAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_share_point_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSharePointAction"]
            )
        )
    if "MSTeamsAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["ms_teams_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["MSTeamsAction"]
            )
        )
    if "CreateAndUpdateMSTeamsAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_ms_teams_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMSTeamsAction"]
            )
        )
    if "ShareMSTeamsAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_ms_teams_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareMSTeamsAction"]
            )
        )
    if "UseMSTeamsAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_ms_teams_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseMSTeamsAction"]
            )
        )
    if "GoogleCalendarAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["google_calendar_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["GoogleCalendarAction"]
            )
        )
    if "CreateAndUpdateGoogleCalendarAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_google_calendar_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleCalendarAction"]
            )
        )
    if "ShareGoogleCalendarAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_google_calendar_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleCalendarAction"]
            )
        )
    if "UseGoogleCalendarAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_google_calendar_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleCalendarAction"]
            )
        )
    if "ZendeskAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["zendesk_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ZendeskAction"]
            )
        )
    if "CreateAndUpdateZendeskAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_zendesk_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateZendeskAction"]
            )
        )
    if "ShareZendeskAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_zendesk_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareZendeskAction"]
            )
        )
    if "UseZendeskAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_zendesk_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseZendeskAction"]
            )
        )
    if "SmartsheetAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["smartsheet_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SmartsheetAction"]
            )
        )
    if "CreateAndUpdateSmartsheetAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_smartsheet_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSmartsheetAction"]
            )
        )
    if "ShareSmartsheetAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_smartsheet_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSmartsheetAction"]
            )
        )
    if "UseSmartsheetAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_smartsheet_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSmartsheetAction"]
            )
        )
    if "SAPBusinessPartnerAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["sap_business_partner_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SAPBusinessPartnerAction"]
            )
        )
    if "CreateAndUpdateSAPBusinessPartnerAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_sap_business_partner_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPBusinessPartnerAction"]
            )
        )
    if "ShareSAPBusinessPartnerAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_sap_business_partner_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPBusinessPartnerAction"]
            )
        )
    if "UseSAPBusinessPartnerAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_sap_business_partner_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSAPBusinessPartnerAction"]
            )
        )
    if "SAPProductMasterDataAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["sap_product_master_data_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SAPProductMasterDataAction"]
            )
        )
    if "CreateAndUpdateSAPProductMasterDataAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_sap_product_master_data_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPProductMasterDataAction"]
            )
        )
    if "ShareSAPProductMasterDataAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_sap_product_master_data_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPProductMasterDataAction"]
            )
        )
    if "UseSAPProductMasterDataAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_sap_product_master_data_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSAPProductMasterDataAction"]
            )
        )
    if "SAPPhysicalInventoryAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["sap_physical_inventory_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SAPPhysicalInventoryAction"]
            )
        )
    if "CreateAndUpdateSAPPhysicalInventoryAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_sap_physical_inventory_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPPhysicalInventoryAction"]
            )
        )
    if "ShareSAPPhysicalInventoryAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_sap_physical_inventory_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPPhysicalInventoryAction"]
            )
        )
    if "UseSAPPhysicalInventoryAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_sap_physical_inventory_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSAPPhysicalInventoryAction"]
            )
        )
    if "SAPBillOfMaterialAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["sap_bill_of_material_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SAPBillOfMaterialAction"]
            )
        )
    if "CreateAndUpdateSAPBillOfMaterialAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_sap_bill_of_material_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPBillOfMaterialAction"]
            )
        )
    if "ShareSAPBillOfMaterialAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_sap_bill_of_material_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPBillOfMaterialAction"]
            )
        )
    if "UseSAPBillOfMaterialAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_sap_bill_of_material_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSAPBillOfMaterialAction"]
            )
        )
    if "SAPMaterialStockAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["sap_material_stock_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SAPMaterialStockAction"]
            )
        )
    if "CreateAndUpdateSAPMaterialStockAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_sap_material_stock_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPMaterialStockAction"]
            )
        )
    if "ShareSAPMaterialStockAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_sap_material_stock_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPMaterialStockAction"]
            )
        )
    if "UseSAPMaterialStockAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_sap_material_stock_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSAPMaterialStockAction"]
            )
        )
    if "FactSetAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["fact_set_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["FactSetAction"]
            )
        )
    if "CreateAndUpdateFactSetAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_fact_set_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateFactSetAction"]
            )
        )
    if "ShareFactSetAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_fact_set_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareFactSetAction"]
            )
        )
    if "UseFactSetAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_fact_set_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseFactSetAction"]
            )
        )
    if "AmazonSThreeAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["amazon_s_three_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["AmazonSThreeAction"]
            )
        )
    if "CreateAndUpdateAmazonSThreeAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_amazon_s_three_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAmazonSThreeAction"]
            )
        )
    if "ShareAmazonSThreeAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_amazon_s_three_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareAmazonSThreeAction"]
            )
        )
    if "UseAmazonSThreeAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_amazon_s_three_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseAmazonSThreeAction"]
            )
        )
    if "TextractAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["textract_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["TextractAction"]
            )
        )
    if "CreateAndUpdateTextractAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_textract_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateTextractAction"]
            )
        )
    if "ShareTextractAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_textract_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareTextractAction"]
            )
        )
    if "UseTextractAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_textract_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseTextractAction"]
            )
        )
    if "ComprehendAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["comprehend_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ComprehendAction"]
            )
        )
    if "CreateAndUpdateComprehendAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_comprehend_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateComprehendAction"]
            )
        )
    if "ShareComprehendAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_comprehend_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareComprehendAction"]
            )
        )
    if "UseComprehendAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_comprehend_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseComprehendAction"]
            )
        )
    if "ComprehendMedicalAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["comprehend_medical_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ComprehendMedicalAction"]
            )
        )
    if "CreateAndUpdateComprehendMedicalAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_comprehend_medical_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateComprehendMedicalAction"]
            )
        )
    if "ShareComprehendMedicalAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_comprehend_medical_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareComprehendMedicalAction"]
            )
        )
    if "UseComprehendMedicalAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_comprehend_medical_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseComprehendMedicalAction"]
            )
        )
    if "AmazonBedrockARSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["amazon_bedrock_ars_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["AmazonBedrockARSAction"]
            )
        )
    if "CreateAndUpdateAmazonBedrockARSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_amazon_bedrock_ars_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAmazonBedrockARSAction"]
            )
        )
    if "ShareAmazonBedrockARSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_amazon_bedrock_ars_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareAmazonBedrockARSAction"]
            )
        )
    if "UseAmazonBedrockARSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_amazon_bedrock_ars_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseAmazonBedrockARSAction"]
            )
        )
    if "AmazonBedrockFSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["amazon_bedrock_fs_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["AmazonBedrockFSAction"]
            )
        )
    if "CreateAndUpdateAmazonBedrockFSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_amazon_bedrock_fs_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAmazonBedrockFSAction"]
            )
        )
    if "ShareAmazonBedrockFSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_amazon_bedrock_fs_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareAmazonBedrockFSAction"]
            )
        )
    if "UseAmazonBedrockFSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_amazon_bedrock_fs_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseAmazonBedrockFSAction"]
            )
        )
    if "AmazonBedrockKRSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["amazon_bedrock_krs_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["AmazonBedrockKRSAction"]
            )
        )
    if "CreateAndUpdateAmazonBedrockKRSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_amazon_bedrock_krs_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAmazonBedrockKRSAction"]
            )
        )
    if "ShareAmazonBedrockKRSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_amazon_bedrock_krs_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareAmazonBedrockKRSAction"]
            )
        )
    if "UseAmazonBedrockKRSAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_amazon_bedrock_krs_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseAmazonBedrockKRSAction"]
            )
        )
    if "MCPAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["mcp_action"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["MCPAction"]
        )
    if "CreateAndUpdateMCPAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_mcp_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMCPAction"]
            )
        )
    if "ShareMCPAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_mcp_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareMCPAction"]
            )
        )
    if "UseMCPAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_mcp_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseMCPAction"]
            )
        )
    if "OpenAPIAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["open_api_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["OpenAPIAction"]
            )
        )
    if "CreateAndUpdateOpenAPIAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_open_api_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateOpenAPIAction"]
            )
        )
    if "ShareOpenAPIAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_open_api_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareOpenAPIAction"]
            )
        )
    if "UseOpenAPIAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_open_api_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseOpenAPIAction"]
            )
        )
    if "SandPGMIAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["sand_pgmi_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SandPGMIAction"]
            )
        )
    if "CreateAndUpdateSandPGMIAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_sand_pgmi_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSandPGMIAction"]
            )
        )
    if "ShareSandPGMIAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_sand_pgmi_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSandPGMIAction"]
            )
        )
    if "UseSandPGMIAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_sand_pgmi_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSandPGMIAction"]
            )
        )
    if "SandPGlobalEnergyAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["sand_p_global_energy_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SandPGlobalEnergyAction"]
            )
        )
    if "CreateAndUpdateSandPGlobalEnergyAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_sand_p_global_energy_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSandPGlobalEnergyAction"]
            )
        )
    if "ShareSandPGlobalEnergyAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_sand_p_global_energy_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSandPGlobalEnergyAction"]
            )
        )
    if "UseSandPGlobalEnergyAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_sand_p_global_energy_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseSandPGlobalEnergyAction"]
            )
        )
    if "BambooHRAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["bamboo_hr_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["BambooHRAction"]
            )
        )
    if "CreateAndUpdateBambooHRAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_bamboo_hr_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateBambooHRAction"]
            )
        )
    if "ShareBambooHRAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_bamboo_hr_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareBambooHRAction"]
            )
        )
    if "UseBambooHRAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_bamboo_hr_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseBambooHRAction"]
            )
        )
    if "BoxAgentAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["box_agent_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["BoxAgentAction"]
            )
        )
    if "CreateAndUpdateBoxAgentAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_box_agent_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateBoxAgentAction"]
            )
        )
    if "ShareBoxAgentAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_box_agent_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareBoxAgentAction"]
            )
        )
    if "UseBoxAgentAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_box_agent_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseBoxAgentAction"]
            )
        )
    if "CanvaAgentAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["canva_agent_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CanvaAgentAction"]
            )
        )
    if "CreateAndUpdateCanvaAgentAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_canva_agent_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateCanvaAgentAction"]
            )
        )
    if "ShareCanvaAgentAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_canva_agent_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareCanvaAgentAction"]
            )
        )
    if "UseCanvaAgentAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_canva_agent_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseCanvaAgentAction"]
            )
        )
    if "GithubAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["github_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["GithubAction"]
            )
        )
    if "CreateAndUpdateGithubAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_github_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGithubAction"]
            )
        )
    if "ShareGithubAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_github_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareGithubAction"]
            )
        )
    if "UseGithubAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_github_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseGithubAction"]
            )
        )
    if "NotionAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["notion_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["NotionAction"]
            )
        )
    if "CreateAndUpdateNotionAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_notion_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateNotionAction"]
            )
        )
    if "ShareNotionAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_notion_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareNotionAction"]
            )
        )
    if "UseNotionAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_notion_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseNotionAction"]
            )
        )
    if "LinearAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["linear_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["LinearAction"]
            )
        )
    if "CreateAndUpdateLinearAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_linear_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateLinearAction"]
            )
        )
    if "ShareLinearAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_linear_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareLinearAction"]
            )
        )
    if "UseLinearAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_linear_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseLinearAction"]
            )
        )
    if "HuggingFaceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["hugging_face_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["HuggingFaceAction"]
            )
        )
    if "CreateAndUpdateHuggingFaceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_hugging_face_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateHuggingFaceAction"]
            )
        )
    if "ShareHuggingFaceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_hugging_face_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareHuggingFaceAction"]
            )
        )
    if "UseHuggingFaceAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_hugging_face_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseHuggingFaceAction"]
            )
        )
    if "MondayAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["monday_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["MondayAction"]
            )
        )
    if "CreateAndUpdateMondayAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_monday_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMondayAction"]
            )
        )
    if "ShareMondayAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_monday_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareMondayAction"]
            )
        )
    if "UseMondayAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_monday_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseMondayAction"]
            )
        )
    if "HubspotAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["hubspot_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["HubspotAction"]
            )
        )
    if "CreateAndUpdateHubspotAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_hubspot_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateHubspotAction"]
            )
        )
    if "ShareHubspotAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_hubspot_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareHubspotAction"]
            )
        )
    if "UseHubspotAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_hubspot_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseHubspotAction"]
            )
        )
    if "IntercomAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["intercom_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["IntercomAction"]
            )
        )
    if "CreateAndUpdateIntercomAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_intercom_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateIntercomAction"]
            )
        )
    if "ShareIntercomAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_intercom_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareIntercomAction"]
            )
        )
    if "UseIntercomAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_intercom_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseIntercomAction"]
            )
        )
    if "NewRelicAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["new_relic_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["NewRelicAction"]
            )
        )
    if "CreateAndUpdateNewRelicAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_and_update_new_relic_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateNewRelicAction"]
            )
        )
    if "ShareNewRelicAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_new_relic_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareNewRelicAction"]
            )
        )
    if "UseNewRelicAction" in data:
        import aws_sdk_quicksight.types.capability_state

        out["use_new_relic_action"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["UseNewRelicAction"]
            )
        )
    if "Topic" in data:
        import aws_sdk_quicksight.types.capability_state

        out["topic"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Topic"]
        )
    if "EditVisualWithQ" in data:
        import aws_sdk_quicksight.types.capability_state

        out["edit_visual_with_q"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["EditVisualWithQ"]
            )
        )
    if "BuildCalculatedFieldWithQ" in data:
        import aws_sdk_quicksight.types.capability_state

        out["build_calculated_field_with_q"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["BuildCalculatedFieldWithQ"]
            )
        )
    if "CreateDashboardExecutiveSummaryWithQ" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_dashboard_executive_summary_with_q"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateDashboardExecutiveSummaryWithQ"]
            )
        )
    if "Space" in data:
        import aws_sdk_quicksight.types.capability_state

        out["space"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Space"]
        )
    if "CreateSpaces" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_spaces"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateSpaces"]
            )
        )
    if "ShareSpaces" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_spaces"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareSpaces"]
            )
        )
    if "ChatAgent" in data:
        import aws_sdk_quicksight.types.capability_state

        out["chat_agent"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["ChatAgent"]
        )
    if "CreateChatAgents" in data:
        import aws_sdk_quicksight.types.capability_state

        out["create_chat_agents"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["CreateChatAgents"]
            )
        )
    if "ShareChatAgents" in data:
        import aws_sdk_quicksight.types.capability_state

        out["share_chat_agents"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ShareChatAgents"]
            )
        )
    if "Research" in data:
        import aws_sdk_quicksight.types.capability_state

        out["research"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Research"]
        )
    if "SelfUpgradeUserRole" in data:
        import aws_sdk_quicksight.types.capability_state

        out["self_upgrade_user_role"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["SelfUpgradeUserRole"]
            )
        )
    if "Extension" in data:
        import aws_sdk_quicksight.types.capability_state

        out["extension"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Extension"]
        )
    if "ManageSharedFolders" in data:
        import aws_sdk_quicksight.types.capability_state

        out["manage_shared_folders"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["ManageSharedFolders"]
            )
        )
    if "GenerateAnalyses" in data:
        import aws_sdk_quicksight.types.capability_state

        out["generate_analyses"] = (
            aws_sdk_quicksight.types.capability_state.deserialize_json(
                data["GenerateAnalyses"]
            )
        )
    if "Story" in data:
        import aws_sdk_quicksight.types.capability_state

        out["story"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Story"]
        )
    if "Scenario" in data:
        import aws_sdk_quicksight.types.capability_state

        out["scenario"] = aws_sdk_quicksight.types.capability_state.deserialize_json(
            data["Scenario"]
        )
    return out
