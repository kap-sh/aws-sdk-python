"""Generated from Smithy shape ``com.amazonaws.ec2#EnableReachabilityAnalyzerOrganizationSharingResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class EnableReachabilityAnalyzerOrganizationSharingResult(TypedDict):
    return_value: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Returns <code>true</code> if the request succeeds; otherwise, returns an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableReachabilityAnalyzerOrganizationSharingResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "return_value" in value:
        pairs.append(
            (f"{prefix}.ReturnValue", "true" if value["return_value"] else "false")
        )


def deserialize_ec2_query(
    el: Element,
) -> EnableReachabilityAnalyzerOrganizationSharingResult:
    out: EnableReachabilityAnalyzerOrganizationSharingResult = {}  # type: ignore[typeddict-item]
    child_return_value = el.find("ReturnValue")
    if child_return_value is not None:
        out["return_value"] = (child_return_value.text or "").lower() == "true"
    return out
