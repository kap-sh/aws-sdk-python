"""Generated from Smithy shape ``com.amazonaws.datazone#RuleTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_target


class _RuleTarget_domainUnitTarget(TypedDict, closed=True):
    domainUnitTarget: "capo_datazone.types.domain_unit_target.DomainUnitTarget"


RuleTarget: TypeAlias = _RuleTarget_domainUnitTarget


# --- restJson1 ser/de ---
def serialize_json(value: RuleTarget) -> dict:
    if "domainUnitTarget" in value:
        import capo_datazone.types.domain_unit_target

        return {
            "domainUnitTarget": capo_datazone.types.domain_unit_target.serialize_json(
                value["domainUnitTarget"]
            )
        }
    else:
        raise SerializationError("RuleTarget: no variant present")


def deserialize_json(data: dict) -> RuleTarget:
    if "domainUnitTarget" in data:
        import capo_datazone.types.domain_unit_target

        return {
            "domainUnitTarget": capo_datazone.types.domain_unit_target.deserialize_json(
                data["domainUnitTarget"]
            )
        }
    else:
        raise DeserializationError("RuleTarget: no recognized variant key")
