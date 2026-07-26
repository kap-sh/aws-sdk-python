"""Generated from Smithy shape ``com.amazonaws.cloudformation#AccountLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.limit_name
    import capo_cloudformation.types.limit_value


class AccountLimit(TypedDict, closed=True):
    name: NotRequired["capo_cloudformation.types.limit_name.LimitName"]
    """<p>The name of the account limit.</p> <p>Values: <code>ConcurrentResourcesLimit</code> | <code>StackLimit</code> | <code>StackOutputsLimit</code> </p>"""
    value: NotRequired["capo_cloudformation.types.limit_value.LimitValue"]
    """<p>The value that's associated with the account limit name.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountLimit, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> AccountLimit:
    out: AccountLimit = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = int(child_value.text or "")
    return out
