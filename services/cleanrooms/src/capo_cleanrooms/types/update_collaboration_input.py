"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateCollaborationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analytics_engine
    import capo_cleanrooms.types.collaboration_description
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.collaboration_name


class UpdateCollaborationInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The identifier for the collaboration.</p>"""
    name: NotRequired["capo_cleanrooms.types.collaboration_name.CollaborationName"]
    """<p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
    ]
    """<p>A description of the collaboration.</p>"""
    analytics_engine: NotRequired[
        "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
    ]
    """<p>The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCollaborationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "analytics_engine" in value:
        import capo_cleanrooms.types.analytics_engine

        out["analyticsEngine"] = capo_cleanrooms.types.analytics_engine.serialize_json(
            value["analytics_engine"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCollaborationInput:
    out: UpdateCollaborationInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "analyticsEngine" in data:
        import capo_cleanrooms.types.analytics_engine

        out["analytics_engine"] = (
            capo_cleanrooms.types.analytics_engine.deserialize_json(
                data["analyticsEngine"]
            )
        )
    return out
