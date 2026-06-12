"""Generated from Smithy shape ``com.amazonaws.cloudformation#EstimateTemplateCostOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.url


class EstimateTemplateCostOutput(TypedDict):
    url: NotRequired["aws_sdk_cloudformation.types.url.Url"]
    """<p>An Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EstimateTemplateCostOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "url" in value:
        pairs.append((f"{prefix}.Url", str(value["url"])))


def deserialize_query(el: Element) -> EstimateTemplateCostOutput:
    out: EstimateTemplateCostOutput = {}  # type: ignore[typeddict-item]
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    return out
