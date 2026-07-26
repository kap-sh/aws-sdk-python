"""Generated from Smithy shape ``com.amazonaws.ec2#GetFlowLogsIntegrationTemplateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class GetFlowLogsIntegrationTemplateResult(TypedDict, closed=True):
    result: NotRequired["capo_ec2.types.string.String"]
    """<p>The generated CloudFormation template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetFlowLogsIntegrationTemplateResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "result" in value:
        pairs.append((f"{prefix}.Result", str(value["result"])))


def deserialize_ec2_query(el: Element) -> GetFlowLogsIntegrationTemplateResult:
    out: GetFlowLogsIntegrationTemplateResult = {}  # type: ignore[typeddict-item]
    child_result = el.find("Result")
    if child_result is not None:
        out["result"] = str(child_result.text or "")
    return out
