"""Generated from Smithy shape ``com.amazonaws.iam#CreateAccessKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.access_key


class CreateAccessKeyResponse(TypedDict, closed=True):
    access_key: "capo_iam.types.access_key.AccessKey"
    """<p>A structure with details about the access key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateAccessKeyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.access_key

    capo_iam.types.access_key.serialize_query(
        value["access_key"], pairs, f"{prefix}.AccessKey"
    )


def deserialize_query(el: Element) -> CreateAccessKeyResponse:
    out: CreateAccessKeyResponse = {}  # type: ignore[typeddict-item]
    child_access_key = el.find("AccessKey")
    if child_access_key is not None:
        import capo_iam.types.access_key

        out["access_key"] = capo_iam.types.access_key.deserialize_query(
            child_access_key
        )
    else:
        raise DeserializationError("CreateAccessKeyResponse.access_key required")
    return out
