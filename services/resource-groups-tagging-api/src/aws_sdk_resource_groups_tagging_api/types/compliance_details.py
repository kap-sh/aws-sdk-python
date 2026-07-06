"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ComplianceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.compliance_status
    import aws_sdk_resource_groups_tagging_api.types.tag_key_list


class ComplianceDetails(TypedDict, closed=True):
    noncompliant_keys: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.tag_key_list.TagKeyList"
    ]
    """<p>These tag keys on the resource are noncompliant with the effective tag policy.</p>"""
    keys_with_noncompliant_values: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.tag_key_list.TagKeyList"
    ]
    """<p>These are keys defined in the effective policy that are on the resource with either incorrect case treatment or noncompliant values. </p>"""
    missing_tag_keys: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.tag_key_list.TagKeyList"
    ]
    """<p>These tag keys are defined as required in the <code>report_required_tag_for</code> block of the effective tag policy, but are missing from the resource.</p>"""
    compliance_status: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.compliance_status.ComplianceStatus"
    ]
    """<p>Whether a resource is compliant with the effective tag policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceDetails) -> dict:
    out: dict = {}
    if "noncompliant_keys" in value:
        import aws_sdk_resource_groups_tagging_api.types.tag_key_list

        out["NoncompliantKeys"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_key_list.serialize_aws_json_1_1(
                value["noncompliant_keys"]
            )
        )
    if "keys_with_noncompliant_values" in value:
        import aws_sdk_resource_groups_tagging_api.types.tag_key_list

        out["KeysWithNoncompliantValues"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_key_list.serialize_aws_json_1_1(
                value["keys_with_noncompliant_values"]
            )
        )
    if "missing_tag_keys" in value:
        import aws_sdk_resource_groups_tagging_api.types.tag_key_list

        out["MissingTagKeys"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_key_list.serialize_aws_json_1_1(
                value["missing_tag_keys"]
            )
        )
    if "compliance_status" in value:
        out["ComplianceStatus"] = value["compliance_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceDetails:
    out: ComplianceDetails = {}  # type: ignore[typeddict-item]
    if "NoncompliantKeys" in data:
        import aws_sdk_resource_groups_tagging_api.types.tag_key_list

        out["noncompliant_keys"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_key_list.deserialize_aws_json_1_1(
                data["NoncompliantKeys"]
            )
        )
    if "KeysWithNoncompliantValues" in data:
        import aws_sdk_resource_groups_tagging_api.types.tag_key_list

        out["keys_with_noncompliant_values"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_key_list.deserialize_aws_json_1_1(
                data["KeysWithNoncompliantValues"]
            )
        )
    if "MissingTagKeys" in data:
        import aws_sdk_resource_groups_tagging_api.types.tag_key_list

        out["missing_tag_keys"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_key_list.deserialize_aws_json_1_1(
                data["MissingTagKeys"]
            )
        )
    if "ComplianceStatus" in data:
        out["compliance_status"] = data["ComplianceStatus"]
    return out
