"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOf__TimezoneEstimationMethodsElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__timezone_estimation_methods_element

ListOf__TimezoneEstimationMethodsElement: TypeAlias = list[
    "capo_pinpoint.types.__timezone_estimation_methods_element.__TimezoneEstimationMethodsElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOf__TimezoneEstimationMethodsElement) -> list:
    import capo_pinpoint.types.__timezone_estimation_methods_element

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint.types.__timezone_estimation_methods_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOf__TimezoneEstimationMethodsElement:
    import capo_pinpoint.types.__timezone_estimation_methods_element

    out: ListOf__TimezoneEstimationMethodsElement = []
    for item in data:
        out.append(
            capo_pinpoint.types.__timezone_estimation_methods_element.deserialize_json(
                item
            )
        )
    return out
