"""Generated from Smithy shape ``com.amazonaws.inspector#RemoveAttributesFromFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.add_remove_attributes_finding_arn_list
    import aws_sdk_inspector.types.user_attribute_key_list


class RemoveAttributesFromFindingsRequest(TypedDict, closed=True):
    finding_arns: "aws_sdk_inspector.types.add_remove_attributes_finding_arn_list.AddRemoveAttributesFindingArnList"
    """<p>The ARNs that specify the findings that you want to remove attributes from.</p>"""
    attribute_keys: (
        "aws_sdk_inspector.types.user_attribute_key_list.UserAttributeKeyList"
    )
    """<p>The array of attribute keys that you want to remove from specified findings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveAttributesFromFindingsRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.add_remove_attributes_finding_arn_list

    out["findingArns"] = (
        aws_sdk_inspector.types.add_remove_attributes_finding_arn_list.serialize_aws_json_1_1(
            value["finding_arns"]
        )
    )
    import aws_sdk_inspector.types.user_attribute_key_list

    out["attributeKeys"] = (
        aws_sdk_inspector.types.user_attribute_key_list.serialize_aws_json_1_1(
            value["attribute_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveAttributesFromFindingsRequest:
    out: RemoveAttributesFromFindingsRequest = {}  # type: ignore[typeddict-item]
    if "findingArns" in data:
        import aws_sdk_inspector.types.add_remove_attributes_finding_arn_list

        out["finding_arns"] = (
            aws_sdk_inspector.types.add_remove_attributes_finding_arn_list.deserialize_aws_json_1_1(
                data["findingArns"]
            )
        )
    else:
        raise DeserializationError(
            "RemoveAttributesFromFindingsRequest.finding_arns required"
        )
    if "attributeKeys" in data:
        import aws_sdk_inspector.types.user_attribute_key_list

        out["attribute_keys"] = (
            aws_sdk_inspector.types.user_attribute_key_list.deserialize_aws_json_1_1(
                data["attributeKeys"]
            )
        )
    else:
        raise DeserializationError(
            "RemoveAttributesFromFindingsRequest.attribute_keys required"
        )
    return out
