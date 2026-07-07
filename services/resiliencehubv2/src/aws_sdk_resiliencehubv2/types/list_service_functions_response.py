"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListServiceFunctionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.service_function_list


class ListServiceFunctionsResponse(TypedDict, closed=True):
    service_functions: (
        "aws_sdk_resiliencehubv2.types.service_function_list.ServiceFunctionList"
    )
    """<p>The list of service functions.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceFunctionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.service_function_list

    out["serviceFunctions"] = (
        aws_sdk_resiliencehubv2.types.service_function_list.serialize_json(
            value["service_functions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceFunctionsResponse:
    out: ListServiceFunctionsResponse = {}  # type: ignore[typeddict-item]
    if "serviceFunctions" in data:
        import aws_sdk_resiliencehubv2.types.service_function_list

        out["service_functions"] = (
            aws_sdk_resiliencehubv2.types.service_function_list.deserialize_json(
                data["serviceFunctions"]
            )
        )
    else:
        raise DeserializationError(
            "ListServiceFunctionsResponse.service_functions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
