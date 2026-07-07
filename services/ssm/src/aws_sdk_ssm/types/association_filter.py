"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_filter_key
    import aws_sdk_ssm.types.association_filter_value


class AssociationFilter(TypedDict, closed=True):
    key: "aws_sdk_ssm.types.association_filter_key.AssociationFilterKey"
    """<p>The name of the filter.</p> <note> <p> <code>InstanceId</code> has been deprecated.</p> </note>"""
    value: "aws_sdk_ssm.types.association_filter_value.AssociationFilterValue"
    """<p>The filter value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationFilter) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.association_filter_key

    out["key"] = aws_sdk_ssm.types.association_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationFilter:
    out: AssociationFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_ssm.types.association_filter_key

        out["key"] = aws_sdk_ssm.types.association_filter_key.deserialize_aws_json_1_1(
            data["key"]
        )
    else:
        raise DeserializationError("AssociationFilter.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("AssociationFilter.value required")
    return out
