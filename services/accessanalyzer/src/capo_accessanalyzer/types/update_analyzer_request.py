"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UpdateAnalyzerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_configuration
    import capo_accessanalyzer.types.analyzer_name


class UpdateAnalyzerRequest(TypedDict, closed=True):
    analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer to modify.</p>"""
    configuration: NotRequired[
        "capo_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnalyzerRequest) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            capo_accessanalyzer.types.analyzer_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAnalyzerRequest:
    out: UpdateAnalyzerRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import capo_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            capo_accessanalyzer.types.analyzer_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
