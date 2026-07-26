"""Generated from Smithy shape ``com.amazonaws.panorama#ListApplicationInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.application_instances
    import capo_panorama.types.next_token


class ListApplicationInstancesResponse(TypedDict, closed=True):
    application_instances: NotRequired[
        "capo_panorama.types.application_instances.ApplicationInstances"
    ]
    """<p>A list of application instances.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationInstancesResponse) -> dict:
    out: dict = {}
    if "application_instances" in value:
        import capo_panorama.types.application_instances

        out["ApplicationInstances"] = (
            capo_panorama.types.application_instances.serialize_json(
                value["application_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationInstancesResponse:
    out: ListApplicationInstancesResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationInstances" in data:
        import capo_panorama.types.application_instances

        out["application_instances"] = (
            capo_panorama.types.application_instances.deserialize_json(
                data["ApplicationInstances"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
