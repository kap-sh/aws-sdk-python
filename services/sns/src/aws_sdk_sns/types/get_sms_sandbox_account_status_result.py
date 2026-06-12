"""Generated from Smithy shape ``com.amazonaws.sns#GetSMSSandboxAccountStatusResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.boolean


class GetSMSSandboxAccountStatusResult(TypedDict):
    is_in_sandbox: "aws_sdk_sns.types.boolean.boolean"
    """<p>Indicates whether the calling Amazon Web Services account is in the SMS sandbox.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSMSSandboxAccountStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (
            f"{prefix}.IsInSandbox",
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
