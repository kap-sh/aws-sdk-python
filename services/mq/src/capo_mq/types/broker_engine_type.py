"""Generated from Smithy shape ``com.amazonaws.mq#BrokerEngineType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__list_of_engine_version
    import capo_mq.types.engine_type


class BrokerEngineType(TypedDict, closed=True):
    engine_type: NotRequired["capo_mq.types.engine_type.EngineType"]
    """<p>The broker's engine type.</p>"""
    engine_versions: NotRequired[
        "capo_mq.types.__list_of_engine_version.__listOfEngineVersion"
    ]
    """<p>The list of engine versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerEngineType) -> dict:
    out: dict = {}
    if "engine_type" in value:
        import capo_mq.types.engine_type

        out["engineType"] = capo_mq.types.engine_type.serialize_json(
            value["engine_type"]
        )
    if "engine_versions" in value:
        import capo_mq.types.__list_of_engine_version

        out["engineVersions"] = capo_mq.types.__list_of_engine_version.serialize_json(
            value["engine_versions"]
        )
    return out


def deserialize_json(data: dict) -> BrokerEngineType:
    out: BrokerEngineType = {}  # type: ignore[typeddict-item]
    if "engineType" in data:
        import capo_mq.types.engine_type

        out["engine_type"] = capo_mq.types.engine_type.deserialize_json(
            data["engineType"]
        )
    if "engineVersions" in data:
        import capo_mq.types.__list_of_engine_version

        out["engine_versions"] = (
            capo_mq.types.__list_of_engine_version.deserialize_json(
                data["engineVersions"]
            )
        )
    return out
