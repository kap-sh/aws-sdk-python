"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ContextKeySelector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.operator_target_list
    import aws_sdk_cloudtrail.types.type


class ContextKeySelector(TypedDict, closed=True):
    type: "aws_sdk_cloudtrail.types.type.Type"
    """<p>Specifies the type of the event record field in ContextKeySelector. Valid values include RequestContext, TagContext.</p>"""
    equals: "aws_sdk_cloudtrail.types.operator_target_list.OperatorTargetList"
    """<p>A list of keys defined by Type to be included in CloudTrail enriched events. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContextKeySelector) -> dict:
    out: dict = {}
    import aws_sdk_cloudtrail.types.type

    out["Type"] = aws_sdk_cloudtrail.types.type.serialize_aws_json_1_1(value["type"])
    import aws_sdk_cloudtrail.types.operator_target_list

    out["Equals"] = (
        aws_sdk_cloudtrail.types.operator_target_list.serialize_aws_json_1_1(
            value["equals"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContextKeySelector:
    out: ContextKeySelector = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_cloudtrail.types.type

        out["type"] = aws_sdk_cloudtrail.types.type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("ContextKeySelector.type required")
    if "Equals" in data:
        import aws_sdk_cloudtrail.types.operator_target_list

        out["equals"] = (
            aws_sdk_cloudtrail.types.operator_target_list.deserialize_aws_json_1_1(
                data["Equals"]
            )
        )
    else:
        raise DeserializationError("ContextKeySelector.equals required")
    return out
