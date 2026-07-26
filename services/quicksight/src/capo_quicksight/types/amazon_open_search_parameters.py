"""Generated from Smithy shape ``com.amazonaws.quicksight#AmazonOpenSearchParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.domain


class AmazonOpenSearchParameters(TypedDict, closed=True):
    domain: "capo_quicksight.types.domain.Domain"
    """<p>The OpenSearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonOpenSearchParameters) -> dict:
    out: dict = {}
    out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> AmazonOpenSearchParameters:
    out: AmazonOpenSearchParameters = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("AmazonOpenSearchParameters.domain required")
    return out
