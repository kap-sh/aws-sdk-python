"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetWorkingLocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.location_type


class GetWorkingLocationRequest(TypedDict, closed=True):
    location_type: NotRequired["aws_sdk_finspace_data.types.location_type.locationType"]
    """<p>Specify the type of the working location.</p> <ul> <li> <p> <code>SAGEMAKER</code> – Use the Amazon S3 location as a temporary location to store data content when working with FinSpace Notebooks that run on SageMaker studio.</p> </li> <li> <p> <code>INGESTION</code> – Use the Amazon S3 location as a staging location to copy your data content and then use the location with the Changeset creation operation.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkingLocationRequest) -> dict:
    out: dict = {}
    if "location_type" in value:
        import aws_sdk_finspace_data.types.location_type

        out["locationType"] = aws_sdk_finspace_data.types.location_type.serialize_json(
            value["location_type"]
        )
    return out


def deserialize_json(data: dict) -> GetWorkingLocationRequest:
    out: GetWorkingLocationRequest = {}  # type: ignore[typeddict-item]
    if "locationType" in data:
        import aws_sdk_finspace_data.types.location_type

        out["location_type"] = (
            aws_sdk_finspace_data.types.location_type.deserialize_json(
                data["locationType"]
            )
        )
    return out
