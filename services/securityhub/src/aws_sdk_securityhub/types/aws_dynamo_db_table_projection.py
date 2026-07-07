"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableProjection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsDynamoDbTableProjection(TypedDict, closed=True):
    non_key_attributes: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>The nonkey attributes that are projected into the index. For each attribute, provide the attribute name.</p>"""
    projection_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The types of attributes that are projected into the index. Valid values are as follows:</p> <ul> <li> <p> <code>ALL</code> </p> </li> <li> <p> <code>INCLUDE</code> </p> </li> <li> <p> <code>KEYS_ONLY</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableProjection) -> dict:
    out: dict = {}
    if "non_key_attributes" in value:
        import aws_sdk_securityhub.types.string_list

        out["NonKeyAttributes"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["non_key_attributes"]
        )
    if "projection_type" in value:
        out["ProjectionType"] = value["projection_type"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableProjection:
    out: AwsDynamoDbTableProjection = {}  # type: ignore[typeddict-item]
    if "NonKeyAttributes" in data:
        import aws_sdk_securityhub.types.string_list

        out["non_key_attributes"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["NonKeyAttributes"]
            )
        )
    if "ProjectionType" in data:
        out["projection_type"] = data["ProjectionType"]
    return out
