"""Generated from Smithy shape ``com.amazonaws.eks#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class Certificate(TypedDict, closed=True):
    data: NotRequired["capo_eks.types.string.String"]
    """<p>The Base64-encoded certificate data required to communicate with your cluster. Add this to the <code>certificate-authority-data</code> section of the <code>kubeconfig</code> file for your cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Certificate) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_json(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if "data" in data:
        out["data"] = data["data"]
    return out
