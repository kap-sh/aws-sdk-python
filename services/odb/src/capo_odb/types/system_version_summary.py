"""Generated from Smithy shape ``com.amazonaws.odb#SystemVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.string_list


class SystemVersionSummary(TypedDict, closed=True):
    gi_version: NotRequired["str"]
    """<p>The version of GI software.</p>"""
    shape: NotRequired["str"]
    """<p>The Exadata hardware model.</p>"""
    system_versions: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The Exadata system versions that are compatible with the specified Exadata shape and GI version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SystemVersionSummary) -> dict:
    out: dict = {}
    if "gi_version" in value:
        out["giVersion"] = value["gi_version"]
    if "shape" in value:
        out["shape"] = value["shape"]
    if "system_versions" in value:
        import capo_odb.types.string_list

        out["systemVersions"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["system_versions"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SystemVersionSummary:
    out: SystemVersionSummary = {}  # type: ignore[typeddict-item]
    if "giVersion" in data:
        out["gi_version"] = data["giVersion"]
    if "shape" in data:
        out["shape"] = data["shape"]
    if "systemVersions" in data:
        import capo_odb.types.string_list

        out["system_versions"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["systemVersions"]
        )
    return out
