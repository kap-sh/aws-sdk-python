"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetAnalyzedResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzed_resource


class GetAnalyzedResourceResponse(TypedDict):
    resource: NotRequired[
        "aws_sdk_accessanalyzer.types.analyzed_resource.AnalyzedResource"
    ]
    """<p>An <code>AnalyzedResource</code> object that contains information that IAM Access Analyzer found when it analyzed the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnalyzedResourceResponse) -> dict:
    out: dict = {}
    if "resource" in value:
        import aws_sdk_accessanalyzer.types.analyzed_resource

        out["resource"] = aws_sdk_accessanalyzer.types.analyzed_resource.serialize_json(
            value["resource"]
        )
    return out


def deserialize_json(data: dict) -> GetAnalyzedResourceResponse:
    out: GetAnalyzedResourceResponse = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        import aws_sdk_accessanalyzer.types.analyzed_resource

        out["resource"] = (
            aws_sdk_accessanalyzer.types.analyzed_resource.deserialize_json(
                data["resource"]
            )
        )
    return out
