"""Generated from Smithy shape ``com.amazonaws.kms#XksKeyConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.xks_key_id_type


class XksKeyConfigurationType(TypedDict, closed=True):
    id: NotRequired["capo_kms.types.xks_key_id_type.XksKeyIdType"]
    """<p>The ID of the external key in its external key manager. This is the ID that the external key store proxy uses to identify the external key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XksKeyConfigurationType) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> XksKeyConfigurationType:
    out: XksKeyConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
