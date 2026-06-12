"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GraphDisplayConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.visual_type


class GraphDisplayConfig(TypedDict):
    visual_type: "aws_sdk_bcm_dashboards.types.visual_type.VisualType"
    """<p>The type of visualization to use for the data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GraphDisplayConfig) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.visual_type

    out["visualType"] = aws_sdk_bcm_dashboards.types.visual_type.serialize_aws_json_1_0(
        value["visual_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GraphDisplayConfig:
    out: GraphDisplayConfig = {}  # type: ignore[typeddict-item]
    if "visualType" in data:
        import aws_sdk_bcm_dashboards.types.visual_type

        out["visual_type"] = (
            aws_sdk_bcm_dashboards.types.visual_type.deserialize_aws_json_1_0(
                data["visualType"]
            )
        )
    else:
        raise DeserializationError("GraphDisplayConfig.visual_type required")
    return out
