"""Generated from Smithy shape ``com.amazonaws.autoscaling#LoadForecasts``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.load_forecast

LoadForecasts: TypeAlias = list["capo_auto_scaling.types.load_forecast.LoadForecast"]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadForecasts, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.load_forecast

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.load_forecast.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadForecasts:
    import capo_auto_scaling.types.load_forecast

    out: LoadForecasts = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.load_forecast.deserialize_query(child))
    return out


def serialize_query_flat(
    value: LoadForecasts, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.load_forecast

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.load_forecast.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LoadForecasts:
    import capo_auto_scaling.types.load_forecast

    out: LoadForecasts = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.load_forecast.deserialize_query(child))
    return out
