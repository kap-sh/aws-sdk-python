"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMlflowAppsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.account_default_status
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.mlflow_app_status
    import aws_sdk_sagemaker.types.mlflow_version
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_mlflow_app_by
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.string
    import aws_sdk_sagemaker.types.timestamp


class ListMlflowAppsRequest(TypedDict):
    created_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    r"""<p>Use the <code>CreatedAfter</code> filter to only list MLflow Apps created after a specific date and time. Listed MLflow Apps are shown with a date and time such as <code>\"2024-03-16T01:46:56+00:00\"</code>. The <code>CreatedAfter</code> parameter takes in a Unix timestamp.</p>"""
    created_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    r"""<p>Use the <code>CreatedBefore</code> filter to only list MLflow Apps created before a specific date and time. Listed MLflow Apps are shown with a date and time such as <code>\"2024-03-16T01:46:56+00:00\"</code>. The <code>CreatedAfter</code> parameter takes in a Unix timestamp.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.mlflow_app_status.MlflowAppStatus"]
    """<p>Filter for Mlflow apps with a specific creation status.</p>"""
    mlflow_version: NotRequired["aws_sdk_sagemaker.types.mlflow_version.MlflowVersion"]
    """<p>Filter for Mlflow Apps with the specified version.</p>"""
    default_for_domain_id: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>Filter for MLflow Apps with the specified default SageMaker Domain ID.</p>"""
    account_default_status: NotRequired[
        "aws_sdk_sagemaker.types.account_default_status.AccountDefaultStatus"
    ]
    """<p>Filter for MLflow Apps with the specified <code>AccountDefaultStatus</code>.</p>"""
    sort_by: NotRequired["aws_sdk_sagemaker.types.sort_mlflow_app_by.SortMlflowAppBy"]
    """<p>Filter for MLflow Apps sorting by name, creation time, or creation status.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>Change the order of the listed MLflow Apps. By default, MLflow Apps are listed in <code>Descending</code> order by creation time. To change the list order, specify <code>SortOrder</code> to be <code>Ascending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, use this token in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of MLflow Apps to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMlflowAppsRequest) -> dict:
    out: dict = {}
    if "created_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "status" in value:
        import aws_sdk_sagemaker.types.mlflow_app_status

        out["Status"] = (
            aws_sdk_sagemaker.types.mlflow_app_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "mlflow_version" in value:
        out["MlflowVersion"] = value["mlflow_version"]
    if "default_for_domain_id" in value:
        out["DefaultForDomainId"] = value["default_for_domain_id"]
    if "account_default_status" in value:
        import aws_sdk_sagemaker.types.account_default_status

        out["AccountDefaultStatus"] = (
            aws_sdk_sagemaker.types.account_default_status.serialize_aws_json_1_1(
                value["account_default_status"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_mlflow_app_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.sort_mlflow_app_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMlflowAppsRequest:
    out: ListMlflowAppsRequest = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedBefore"]
            )
        )
    if "Status" in data:
        import aws_sdk_sagemaker.types.mlflow_app_status

        out["status"] = (
            aws_sdk_sagemaker.types.mlflow_app_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "MlflowVersion" in data:
        out["mlflow_version"] = data["MlflowVersion"]
    if "DefaultForDomainId" in data:
        out["default_for_domain_id"] = data["DefaultForDomainId"]
    if "AccountDefaultStatus" in data:
        import aws_sdk_sagemaker.types.account_default_status

        out["account_default_status"] = (
            aws_sdk_sagemaker.types.account_default_status.deserialize_aws_json_1_1(
                data["AccountDefaultStatus"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_mlflow_app_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.sort_mlflow_app_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
