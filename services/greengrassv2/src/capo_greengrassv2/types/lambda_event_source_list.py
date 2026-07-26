"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaEventSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.lambda_event_source

LambdaEventSourceList: TypeAlias = list[
    "capo_greengrassv2.types.lambda_event_source.LambdaEventSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaEventSourceList) -> list:
    import capo_greengrassv2.types.lambda_event_source

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.lambda_event_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> LambdaEventSourceList:
    import capo_greengrassv2.types.lambda_event_source

    out: LambdaEventSourceList = []
    for item in data:
        out.append(capo_greengrassv2.types.lambda_event_source.deserialize_json(item))
    return out
