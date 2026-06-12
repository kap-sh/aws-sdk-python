"""Generated from Smithy shape ``com.amazonaws.sustainability#EstimatedCarbonEmissions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.dimensions_map
    import aws_sdk_sustainability.types.emissions_map
    import aws_sdk_sustainability.types.model_version
    import aws_sdk_sustainability.types.time_period


class EstimatedCarbonEmissions(TypedDict):
    time_period: "aws_sdk_sustainability.types.time_period.TimePeriod"
    """<p>The reporting period for emission values.</p>"""
    dimensions_values: "aws_sdk_sustainability.types.dimensions_map.DimensionsMap"
    """<p>The dimensions used to group emissions values.</p>"""
    model_version: "aws_sdk_sustainability.types.model_version.ModelVersion"
    """<p>The semantic version-formatted string that indicates the methodology version used to calculate the emission values. </p> <note> <p> The AWS Sustainability service reflects the most recent model version for every month. You will not see two entries for the same month with different <code>ModelVersion</code> values. To track the evolution of the methodology and compare emission values from previous versions, we recommend creating a <a href=\"https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html\">Data Export</a>. </p> </note>"""
    emissions_values: "aws_sdk_sustainability.types.emissions_map.EmissionsMap"
    """<p>The emissions values for the requested emissions types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EstimatedCarbonEmissions) -> dict:
    out: dict = {}
    import aws_sdk_sustainability.types.time_period

    out["TimePeriod"] = aws_sdk_sustainability.types.time_period.serialize_json(
        value["time_period"]
    )
    import aws_sdk_sustainability.types.dimensions_map

    out["DimensionsValues"] = (
        aws_sdk_sustainability.types.dimensions_map.serialize_json(
            value["dimensions_values"]
        )
    )
    out["ModelVersion"] = value["model_version"]
    import aws_sdk_sustainability.types.emissions_map

    out["EmissionsValues"] = aws_sdk_sustainability.types.emissions_map.serialize_json(
        value["emissions_values"]
    )
    return out


def deserialize_json(data: dict) -> EstimatedCarbonEmissions:
    out: EstimatedCarbonEmissions = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import aws_sdk_sustainability.types.time_period

        out["time_period"] = aws_sdk_sustainability.types.time_period.deserialize_json(
            data["TimePeriod"]
        )
    else:
        raise DeserializationError("EstimatedCarbonEmissions.time_period required")
    if "DimensionsValues" in data:
        import aws_sdk_sustainability.types.dimensions_map

        out["dimensions_values"] = (
            aws_sdk_sustainability.types.dimensions_map.deserialize_json(
                data["DimensionsValues"]
            )
        )
    else:
        raise DeserializationError(
            "EstimatedCarbonEmissions.dimensions_values required"
        )
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    else:
        raise DeserializationError("EstimatedCarbonEmissions.model_version required")
    if "EmissionsValues" in data:
        import aws_sdk_sustainability.types.emissions_map

        out["emissions_values"] = (
            aws_sdk_sustainability.types.emissions_map.deserialize_json(
                data["EmissionsValues"]
            )
        )
    else:
        raise DeserializationError("EstimatedCarbonEmissions.emissions_values required")
    return out
