"""Generated from Smithy shape ``com.amazonaws.quicksight#QDataKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.q_data_key_type
    import aws_sdk_quicksight.types.string


class QDataKey(TypedDict):
    q_data_key_arn: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The ARN of the KMS key that is registered to a Quick Sight account for encryption and decryption use as a <code>QDataKey</code>.</p>"""
    q_data_key_type: NotRequired[
        "aws_sdk_quicksight.types.q_data_key_type.QDataKeyType"
    ]
    """<p>The type of <code>QDataKey</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QDataKey) -> dict:
    out: dict = {}
    if "q_data_key_arn" in value:
        out["QDataKeyArn"] = value["q_data_key_arn"]
    if "q_data_key_type" in value:
        import aws_sdk_quicksight.types.q_data_key_type

        out["QDataKeyType"] = aws_sdk_quicksight.types.q_data_key_type.serialize_json(
            value["q_data_key_type"]
        )
    return out


def deserialize_json(data: dict) -> QDataKey:
    out: QDataKey = {}  # type: ignore[typeddict-item]
    if "QDataKeyArn" in data:
        out["q_data_key_arn"] = data["QDataKeyArn"]
    if "QDataKeyType" in data:
        import aws_sdk_quicksight.types.q_data_key_type

        out["q_data_key_type"] = (
            aws_sdk_quicksight.types.q_data_key_type.deserialize_json(
                data["QDataKeyType"]
            )
        )
    return out
