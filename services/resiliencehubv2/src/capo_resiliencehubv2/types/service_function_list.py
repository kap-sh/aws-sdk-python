"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunctionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_function

ServiceFunctionList: TypeAlias = list[
    "capo_resiliencehubv2.types.service_function.ServiceFunction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFunctionList) -> list:
    import capo_resiliencehubv2.types.service_function

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.service_function.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceFunctionList:
    import capo_resiliencehubv2.types.service_function

    out: ServiceFunctionList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.service_function.deserialize_json(item))
    return out
