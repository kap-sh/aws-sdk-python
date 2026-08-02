"""Generated from Smithy shape ``com.amazonaws.rds#DescribeEngineDefaultClusterParametersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.engine_defaults


class DescribeEngineDefaultClusterParametersResult(TypedDict, closed=True):
    engine_defaults: NotRequired["capo_rds.types.engine_defaults.EngineDefaults"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEngineDefaultClusterParametersResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "engine_defaults" in value:
        import capo_rds.types.engine_defaults

        capo_rds.types.engine_defaults.serialize_query(
            value["engine_defaults"], pairs, f"{key_prefix}EngineDefaults"
        )


def deserialize_query(el: Element) -> DescribeEngineDefaultClusterParametersResult:
    out: DescribeEngineDefaultClusterParametersResult = {}  # type: ignore[typeddict-item]
    child_engine_defaults = el.find("EngineDefaults")
    if child_engine_defaults is not None:
        import capo_rds.types.engine_defaults

        out["engine_defaults"] = capo_rds.types.engine_defaults.deserialize_query(
            child_engine_defaults
        )
    return out
