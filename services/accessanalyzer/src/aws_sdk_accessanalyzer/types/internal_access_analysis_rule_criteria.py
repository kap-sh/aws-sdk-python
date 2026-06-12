"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessAnalysisRuleCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.account_ids_list
    import aws_sdk_accessanalyzer.types.resource_arns_list
    import aws_sdk_accessanalyzer.types.resource_type_list


class InternalAccessAnalysisRuleCriteria(TypedDict):
    account_ids: NotRequired[
        "aws_sdk_accessanalyzer.types.account_ids_list.AccountIdsList"
    ]
    """<p>A list of Amazon Web Services account IDs to apply to the internal access analysis rule criteria. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers.</p>"""
    resource_types: NotRequired[
        "aws_sdk_accessanalyzer.types.resource_type_list.ResourceTypeList"
    ]
    """<p>A list of resource types to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources of these types. These resource types are currently supported for internal access analyzers:</p> <ul> <li> <p> <code>AWS::S3::Bucket</code> </p> </li> <li> <p> <code>AWS::RDS::DBSnapshot</code> </p> </li> <li> <p> <code>AWS::RDS::DBClusterSnapshot</code> </p> </li> <li> <p> <code>AWS::S3Express::DirectoryBucket</code> </p> </li> <li> <p> <code>AWS::DynamoDB::Table</code> </p> </li> <li> <p> <code>AWS::DynamoDB::Stream</code> </p> </li> </ul>"""
    resource_arns: NotRequired[
        "aws_sdk_accessanalyzer.types.resource_arns_list.ResourceArnsList"
    ]
    """<p>A list of resource ARNs to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources that match these ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalAccessAnalysisRuleCriteria) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_accessanalyzer.types.account_ids_list

        out["accountIds"] = (
            aws_sdk_accessanalyzer.types.account_ids_list.serialize_json(
                value["account_ids"]
            )
        )
    if "resource_types" in value:
        import aws_sdk_accessanalyzer.types.resource_type_list

        out["resourceTypes"] = (
            aws_sdk_accessanalyzer.types.resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    if "resource_arns" in value:
        import aws_sdk_accessanalyzer.types.resource_arns_list

        out["resourceArns"] = (
            aws_sdk_accessanalyzer.types.resource_arns_list.serialize_json(
                value["resource_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> InternalAccessAnalysisRuleCriteria:
    out: InternalAccessAnalysisRuleCriteria = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_accessanalyzer.types.account_ids_list

        out["account_ids"] = (
            aws_sdk_accessanalyzer.types.account_ids_list.deserialize_json(
                data["accountIds"]
            )
        )
    if "resourceTypes" in data:
        import aws_sdk_accessanalyzer.types.resource_type_list

        out["resource_types"] = (
            aws_sdk_accessanalyzer.types.resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    if "resourceArns" in data:
        import aws_sdk_accessanalyzer.types.resource_arns_list

        out["resource_arns"] = (
            aws_sdk_accessanalyzer.types.resource_arns_list.deserialize_json(
                data["resourceArns"]
            )
        )
    return out
