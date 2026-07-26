"""Generated from Smithy shape ``com.amazonaws.outposts#FormFactorConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.form_factor_config

FormFactorConfigList: TypeAlias = list[
    "capo_outposts.types.form_factor_config.FormFactorConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: FormFactorConfigList) -> list:
    import capo_outposts.types.form_factor_config

    out: list = []
    for item in value:
        out.append(capo_outposts.types.form_factor_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> FormFactorConfigList:
    import capo_outposts.types.form_factor_config

    out: FormFactorConfigList = []
    for item in data:
        out.append(capo_outposts.types.form_factor_config.deserialize_json(item))
    return out
