"""Generated from Smithy shape ``com.amazonaws.emr#ListStudioSessionMappingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.identity_type
    import capo_emr.types.marker
    import capo_emr.types.xml_string_max_len256


class ListStudioSessionMappingsInput(TypedDict, closed=True):
    studio_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon EMR Studio.</p>"""
    identity_type: NotRequired["capo_emr.types.identity_type.IdentityType"]
    """<p>Specifies whether to return session mappings for users or groups. If not specified, the results include session mapping details for both users and groups.</p>"""
    marker: NotRequired["capo_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStudioSessionMappingsInput) -> dict:
    out: dict = {}
    if "studio_id" in value:
        out["StudioId"] = value["studio_id"]
    if "identity_type" in value:
        import capo_emr.types.identity_type

        out["IdentityType"] = capo_emr.types.identity_type.serialize_aws_json_1_1(
            value["identity_type"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStudioSessionMappingsInput:
    out: ListStudioSessionMappingsInput = {}  # type: ignore[typeddict-item]
    if "StudioId" in data:
        out["studio_id"] = data["StudioId"]
    if "IdentityType" in data:
        import capo_emr.types.identity_type

        out["identity_type"] = capo_emr.types.identity_type.deserialize_aws_json_1_1(
            data["IdentityType"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
