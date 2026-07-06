"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetVectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.get_vectors_output_list


class GetVectorsOutput(TypedDict, closed=True):
    vectors: "aws_sdk_s3vectors.types.get_vectors_output_list.GetVectorsOutputList"
    """<p>The attributes of the vectors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVectorsOutput) -> dict:
    out: dict = {}
    import aws_sdk_s3vectors.types.get_vectors_output_list

    out["vectors"] = aws_sdk_s3vectors.types.get_vectors_output_list.serialize_json(
        value["vectors"]
    )
    return out


def deserialize_json(data: dict) -> GetVectorsOutput:
    out: GetVectorsOutput = {}  # type: ignore[typeddict-item]
    if "vectors" in data:
        import aws_sdk_s3vectors.types.get_vectors_output_list

        out["vectors"] = (
            aws_sdk_s3vectors.types.get_vectors_output_list.deserialize_json(
                data["vectors"]
            )
        )
    else:
        raise DeserializationError("GetVectorsOutput.vectors required")
    return out
