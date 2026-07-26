"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckToActionsMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.audit_check_name
    import capo_iot.types.mitigation_action_name_list

AuditCheckToActionsMapping: TypeAlias = dict[
    "capo_iot.types.audit_check_name.AuditCheckName",
    "capo_iot.types.mitigation_action_name_list.MitigationActionNameList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuditCheckToActionsMapping) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iot.types.mitigation_action_name_list

        out[key] = capo_iot.types.mitigation_action_name_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AuditCheckToActionsMapping:
    out: AuditCheckToActionsMapping = {}
    for key, value in data.items():
        import capo_iot.types.mitigation_action_name_list

        out[key] = capo_iot.types.mitigation_action_name_list.deserialize_json(value)
    return out
