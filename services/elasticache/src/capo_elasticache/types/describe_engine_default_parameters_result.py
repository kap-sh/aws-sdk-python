"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeEngineDefaultParametersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.engine_defaults


class DescribeEngineDefaultParametersResult(TypedDict, closed=True):
    engine_defaults: NotRequired[
        "capo_elasticache.types.engine_defaults.EngineDefaults"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEngineDefaultParametersResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "engine_defaults" in value:
        import capo_elasticache.types.engine_defaults

        capo_elasticache.types.engine_defaults.serialize_query(
            value["engine_defaults"], pairs, f"{prefix}.EngineDefaults"
        )


def deserialize_query(el: Element) -> DescribeEngineDefaultParametersResult:
    out: DescribeEngineDefaultParametersResult = {}  # type: ignore[typeddict-item]
    child_engine_defaults = el.find("EngineDefaults")
    if child_engine_defaults is not None:
        import capo_elasticache.types.engine_defaults

        out["engine_defaults"] = (
            capo_elasticache.types.engine_defaults.deserialize_query(
                child_engine_defaults
            )
        )
    return out
