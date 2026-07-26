"""Generated from Smithy shape ``com.amazonaws.tnb#NetworkArtifactMeta``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.override_list


class NetworkArtifactMeta(TypedDict, closed=True):
    overrides: NotRequired["capo_tnb.types.override_list.OverrideList"]
    """<p>Lists network package overrides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkArtifactMeta) -> dict:
    out: dict = {}
    if "overrides" in value:
        import capo_tnb.types.override_list

        out["overrides"] = capo_tnb.types.override_list.serialize_json(
            value["overrides"]
        )
    return out


def deserialize_json(data: dict) -> NetworkArtifactMeta:
    out: NetworkArtifactMeta = {}  # type: ignore[typeddict-item]
    if "overrides" in data:
        import capo_tnb.types.override_list

        out["overrides"] = capo_tnb.types.override_list.deserialize_json(
            data["overrides"]
        )
    return out
