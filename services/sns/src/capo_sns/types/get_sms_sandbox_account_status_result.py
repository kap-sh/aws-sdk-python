"""Generated from Smithy shape ``com.amazonaws.sns#GetSMSSandboxAccountStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.boolean


class GetSMSSandboxAccountStatusResult(TypedDict, closed=True):
    is_in_sandbox: "capo_sns.types.boolean.boolean"
    """<p>Indicates whether the calling Amazon Web Services account is in the SMS sandbox.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSMSSandboxAccountStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (
            f"{key_prefix}IsInSandbox",
            "true" if value.get("is_in_sandbox", False) else "false",
        )
    )


def deserialize_query(el: Element) -> GetSMSSandboxAccountStatusResult:
    out: GetSMSSandboxAccountStatusResult = {}  # type: ignore[typeddict-item]
    child_is_in_sandbox = el.find("IsInSandbox")
    if child_is_in_sandbox is not None:
        out["is_in_sandbox"] = (child_is_in_sandbox.text or "").lower() == "true"
    else:
        out["is_in_sandbox"] = False
    return out
