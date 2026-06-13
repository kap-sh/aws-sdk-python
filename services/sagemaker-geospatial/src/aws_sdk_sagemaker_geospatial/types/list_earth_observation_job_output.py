"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListEarthObservationJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_list
    import aws_sdk_sagemaker_geospatial.types.next_token


class ListEarthObservationJobOutput(TypedDict):
    earth_observation_job_summaries: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_list.EarthObservationJobList"
    """<p>Contains summary information about the Earth Observation jobs.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEarthObservationJobOutput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_list

    out["EarthObservationJobSummaries"] = (
        aws_sdk_sagemaker_geospatial.types.earth_observation_job_list.serialize_json(
            value["earth_observation_job_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEarthObservationJobOutput:
    out: ListEarthObservationJobOutput = {}  # type: ignore[typeddict-item]
    if "EarthObservationJobSummaries" in data:
        import aws_sdk_sagemaker_geospatial.types.earth_observation_job_list

        out["earth_observation_job_summaries"] = (
            aws_sdk_sagemaker_geospatial.types.earth_observation_job_list.deserialize_json(
                data["EarthObservationJobSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListEarthObservationJobOutput.earth_observation_job_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
