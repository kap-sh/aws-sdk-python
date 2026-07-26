"""Generated from Smithy shape ``com.amazonaws.quicksight#QDataKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.q_data_key_type
    import capo_quicksight.types.string


class QDataKey(TypedDict, closed=True):
    q_data_key_arn: NotRequired["capo_quicksight.types.string.String"]
    """<p>The ARN of the KMS key that is registered to a Quick Sight account for encryption and decryption use as a <code>QDataKey</code>.</p>"""
    q_data_key_type: NotRequired["capo_quicksight.types.q_data_key_type.QDataKeyType"]
    """<p>The type of <code>QDataKey</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QDataKey) -> dict:
    out: dict = {}
    if "q_data_key_arn" in value:
        out["QDataKeyArn"] = value["q_data_key_arn"]
    if "q_data_key_type" in value:
        import capo_quicksight.types.q_data_key_type

        out["QDataKeyType"] = capo_quicksight.types.q_data_key_type.serialize_json(
            value["q_data_key_type"]
        )
    return out


def deserialize_json(data: dict) -> QDataKey:
    out: QDataKey = {}  # type: ignore[typeddict-item]
    if "QDataKeyArn" in data:
        out["q_data_key_arn"] = data["QDataKeyArn"]
    if "QDataKeyType" in data:
        import capo_quicksight.types.q_data_key_type

        out["q_data_key_type"] = capo_quicksight.types.q_data_key_type.deserialize_json(
            data["QDataKeyType"]
        )
    return out
