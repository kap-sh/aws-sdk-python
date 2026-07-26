"""Generated from Smithy shape ``com.amazonaws.athena#EngineVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.name_string


class EngineVersion(TypedDict, closed=True):
    selected_engine_version: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>The engine version requested by the user. Possible values are determined by the output of <code>ListEngineVersions</code>, including AUTO. The default is AUTO.</p>"""
    effective_engine_version: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>Read only. The engine version on which the query runs. If the user requests a valid engine version other than Auto, the effective engine version is the same as the engine version that the user requested. If the user requests Auto, the effective engine version is chosen by Athena. When a request to update the engine version is made by a <code>CreateWorkGroup</code> or <code>UpdateWorkGroup</code> operation, the <code>EffectiveEngineVersion</code> field is ignored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineVersion) -> dict:
    out: dict = {}
    if "selected_engine_version" in value:
        out["SelectedEngineVersion"] = value["selected_engine_version"]
    if "effective_engine_version" in value:
        out["EffectiveEngineVersion"] = value["effective_engine_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EngineVersion:
    out: EngineVersion = {}  # type: ignore[typeddict-item]
    if "SelectedEngineVersion" in data:
        out["selected_engine_version"] = data["SelectedEngineVersion"]
    if "EffectiveEngineVersion" in data:
        out["effective_engine_version"] = data["EffectiveEngineVersion"]
    return out
