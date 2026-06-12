"""Generated from Smithy shape ``com.amazonaws.sts#GetAccessKeyInfoRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sts.types.access_key_id_type


class GetAccessKeyInfoRequest(TypedDict):
    access_key_id: "aws_sdk_sts.types.access_key_id_type.accessKeyIdType"
    """<p>The identifier of an access key.</p> <p>This parameter allows (through its regex pattern) a string of characters that can consist of any upper- or lowercase letter or digit.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccessKeyInfoRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.AccessKeyId", str(value["access_key_id"])))


def deserialize_query(el: Element) -> GetAccessKeyInfoRequest:
    out: GetAccessKeyInfoRequest = {}  # type: ignore[typeddict-item]
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    else:
        raise DeserializationError("GetAccessKeyInfoRequest.access_key_id required")
    return out
