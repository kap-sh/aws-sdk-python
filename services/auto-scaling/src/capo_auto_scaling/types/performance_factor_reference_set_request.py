"""Generated from Smithy shape ``com.amazonaws.autoscaling#PerformanceFactorReferenceSetRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.performance_factor_reference_request

PerformanceFactorReferenceSetRequest: TypeAlias = list[
    "capo_auto_scaling.types.performance_factor_reference_request.PerformanceFactorReferenceRequest"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PerformanceFactorReferenceSetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_auto_scaling.types.performance_factor_reference_request

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.performance_factor_reference_request.serialize_query(
            item, pairs, f"{prefix}.item.{n}"
        )


def deserialize_query(el: Element) -> PerformanceFactorReferenceSetRequest:
    import capo_auto_scaling.types.performance_factor_reference_request

    out: PerformanceFactorReferenceSetRequest = []
    for child in el.findall("item"):
        out.append(
            capo_auto_scaling.types.performance_factor_reference_request.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PerformanceFactorReferenceSetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_auto_scaling.types.performance_factor_reference_request

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.performance_factor_reference_request.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> PerformanceFactorReferenceSetRequest:
    import capo_auto_scaling.types.performance_factor_reference_request

    out: PerformanceFactorReferenceSetRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.performance_factor_reference_request.deserialize_query(
                child
            )
        )
    return out
