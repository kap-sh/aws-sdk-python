"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardVisualEmbeddingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_visual_id


class AnonymousUserDashboardVisualEmbeddingConfiguration(TypedDict, closed=True):
    initial_dashboard_visual_id: (
        "aws_sdk_quicksight.types.dashboard_visual_id.DashboardVisualId"
    )
    """<p>The visual ID for the visual that you want the user to see. This ID is included in the output URL. When the URL in response is accessed, Amazon Quick Sight renders this visual.</p> <p>The Amazon Resource Name (ARN) of the dashboard that the visual belongs to must be included in the <code>AuthorizedResourceArns</code> parameter. Otherwise, the request will fail with <code>InvalidParameterValueException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnonymousUserDashboardVisualEmbeddingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.dashboard_visual_id

    out["InitialDashboardVisualId"] = (
        aws_sdk_quicksight.types.dashboard_visual_id.serialize_json(
            value["initial_dashboard_visual_id"]
        )
    )
    return out


def deserialize_json(data: dict) -> AnonymousUserDashboardVisualEmbeddingConfiguration:
    out: AnonymousUserDashboardVisualEmbeddingConfiguration = {}  # type: ignore[typeddict-item]
    if "InitialDashboardVisualId" in data:
        import aws_sdk_quicksight.types.dashboard_visual_id

        out["initial_dashboard_visual_id"] = (
            aws_sdk_quicksight.types.dashboard_visual_id.deserialize_json(
                data["InitialDashboardVisualId"]
            )
        )
    else:
        raise DeserializationError(
            "AnonymousUserDashboardVisualEmbeddingConfiguration.initial_dashboard_visual_id required"
        )
    return out
