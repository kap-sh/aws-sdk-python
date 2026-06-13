"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateServiceFunctionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_function


class CreateServiceFunctionResponse(TypedDict):
    service_function: "aws_sdk_resiliencehubv2.types.service_function.ServiceFunction"
    """<p>The created service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceFunctionResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.service_function

    out["serviceFunction"] = (
        aws_sdk_resiliencehubv2.types.service_function.serialize_json(
            value["service_function"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateServiceFunctionResponse:
    out: CreateServiceFunctionResponse = {}  # type: ignore[typeddict-item]
    if "serviceFunction" in data:
        import aws_sdk_resiliencehubv2.types.service_function

        out["service_function"] = (
            aws_sdk_resiliencehubv2.types.service_function.deserialize_json(
                data["serviceFunction"]
            )
        )
    else:
        raise DeserializationError(
            "CreateServiceFunctionResponse.service_function required"
        )
    return out
