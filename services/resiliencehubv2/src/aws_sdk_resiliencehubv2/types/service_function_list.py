"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunctionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_function

ServiceFunctionList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.service_function.ServiceFunction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFunctionList) -> list:
    import aws_sdk_resiliencehubv2.types.service_function

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.service_function.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceFunctionList:
    import aws_sdk_resiliencehubv2.types.service_function

    out: ServiceFunctionList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.service_function.deserialize_json(item)
        )
    return out
