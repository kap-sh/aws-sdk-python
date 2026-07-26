"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ResourceServerScopeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.description


class ResourceServerScopeDetails(TypedDict, closed=True):
    long_description: NotRequired["capo_sso_admin.types.description.Description"]
    """<p>The description of an access scope for a resource server.</p>"""
    detailed_title: NotRequired["capo_sso_admin.types.description.Description"]
    """<p>The title of an access scope for a resource server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceServerScopeDetails) -> dict:
    out: dict = {}
    if "long_description" in value:
        out["LongDescription"] = value["long_description"]
    if "detailed_title" in value:
        out["DetailedTitle"] = value["detailed_title"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceServerScopeDetails:
    out: ResourceServerScopeDetails = {}  # type: ignore[typeddict-item]
    if "LongDescription" in data:
        out["long_description"] = data["LongDescription"]
    if "DetailedTitle" in data:
        out["detailed_title"] = data["DetailedTitle"]
    return out
