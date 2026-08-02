"""Generated from Smithy shape ``com.amazonaws.ec2#OperatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class OperatorRequest(TypedDict, closed=True):
    principal: NotRequired["capo_ec2.types.string.String"]
    """<p>The service provider that manages the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: OperatorRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "principal" in value:
        pairs.append((f"{key_prefix}Principal", str(value["principal"])))


def deserialize_ec2_query(el: Element) -> OperatorRequest:
    out: OperatorRequest = {}  # type: ignore[typeddict-item]
    child_principal = el.find("Principal")
    if child_principal is not None:
        out["principal"] = str(child_principal.text or "")
    return out
