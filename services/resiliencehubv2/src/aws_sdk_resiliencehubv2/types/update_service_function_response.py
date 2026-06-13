"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateServiceFunctionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_function


class UpdateServiceFunctionResponse(TypedDict):
    service_function: "aws_sdk_resiliencehubv2.types.service_function.ServiceFunction"
    """<p>The updated service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceFunctionResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.service_function

    out["serviceFunction"] = (
        aws_sdk_resiliencehubv2.types.service_function.serialize_json(
            value["service_function"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateServiceFunctionResponse:
    out: UpdateServiceFunctionResponse = {}  # type: ignore[typeddict-item]
    if "serviceFunction" in data:
        import aws_sdk_resiliencehubv2.types.service_function

        out["service_function"] = (
            aws_sdk_resiliencehubv2.types.service_function.deserialize_json(
                data["serviceFunction"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceFunctionResponse.service_function required"
        )
    return out
