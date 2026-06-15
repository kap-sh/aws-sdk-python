"""Generated from Smithy shape ``com.amazonaws.iam#GetAccessKeyLastUsedRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.access_key_id_type


class GetAccessKeyLastUsedRequest(TypedDict):
    access_key_id: "aws_sdk_iam.types.access_key_id_type.accessKeyIdType"
    r"""<p>The identifier of an access key.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters that can consist of any upper or lowercased letter or digit.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccessKeyLastUsedRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.AccessKeyId", str(value["access_key_id"])))


def deserialize_query(el: Element) -> GetAccessKeyLastUsedRequest:
    out: GetAccessKeyLastUsedRequest = {}  # type: ignore[typeddict-item]
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    else:
        raise DeserializationError("GetAccessKeyLastUsedRequest.access_key_id required")
    return out
