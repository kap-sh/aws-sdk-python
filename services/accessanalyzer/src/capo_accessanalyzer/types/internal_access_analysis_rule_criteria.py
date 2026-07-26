"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessAnalysisRuleCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.account_ids_list
    import capo_accessanalyzer.types.resource_arns_list
    import capo_accessanalyzer.types.resource_type_list


class InternalAccessAnalysisRuleCriteria(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_accessanalyzer.types.account_ids_list.AccountIdsList"
    ]
    """<p>A list of Amazon Web Services account IDs to apply to the internal access analysis rule criteria. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers.</p>"""
    resource_types: NotRequired[
        "capo_accessanalyzer.types.resource_type_list.ResourceTypeList"
    ]
    """<p>A list of resource types to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources of these types. These resource types are currently supported for internal access analyzers:</p> <ul> <li> <p> <code>AWS::S3::Bucket</code> </p> </li> <li> <p> <code>AWS::RDS::DBSnapshot</code> </p> </li> <li> <p> <code>AWS::RDS::DBClusterSnapshot</code> </p> </li> <li> <p> <code>AWS::S3Express::DirectoryBucket</code> </p> </li> <li> <p> <code>AWS::DynamoDB::Table</code> </p> </li> <li> <p> <code>AWS::DynamoDB::Stream</code> </p> </li> </ul>"""
    resource_arns: NotRequired[
        "capo_accessanalyzer.types.resource_arns_list.ResourceArnsList"
    ]
    """<p>A list of resource ARNs to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources that match these ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalAccessAnalysisRuleCriteria) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_accessanalyzer.types.account_ids_list

        out["accountIds"] = capo_accessanalyzer.types.account_ids_list.serialize_json(
            value["account_ids"]
        )
    if "resource_types" in value:
        import capo_accessanalyzer.types.resource_type_list

        out["resourceTypes"] = (
            capo_accessanalyzer.types.resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    if "resource_arns" in value:
        import capo_accessanalyzer.types.resource_arns_list

        out["resourceArns"] = (
            capo_accessanalyzer.types.resource_arns_list.serialize_json(
                value["resource_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> InternalAccessAnalysisRuleCriteria:
    out: InternalAccessAnalysisRuleCriteria = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import capo_accessanalyzer.types.account_ids_list

        out["account_ids"] = (
            capo_accessanalyzer.types.account_ids_list.deserialize_json(
                data["accountIds"]
            )
        )
    if "resourceTypes" in data:
        import capo_accessanalyzer.types.resource_type_list

        out["resource_types"] = (
            capo_accessanalyzer.types.resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    if "resourceArns" in data:
        import capo_accessanalyzer.types.resource_arns_list

        out["resource_arns"] = (
            capo_accessanalyzer.types.resource_arns_list.deserialize_json(
                data["resourceArns"]
            )
        )
    return out
