"""Generated from Smithy shape ``com.amazonaws.ses#GetAccountSendingEnabledResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.enabled


class GetAccountSendingEnabledResponse(TypedDict, closed=True):
    enabled: "capo_ses.types.enabled.Enabled"
    """<p>Describes whether email sending is enabled or disabled for your Amazon SES account in the current Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccountSendingEnabledResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (f"{prefix}.Enabled", "true" if value.get("enabled", False) else "false")
    )


def deserialize_query(el: Element) -> GetAccountSendingEnabledResponse:
    out: GetAccountSendingEnabledResponse = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    return out
