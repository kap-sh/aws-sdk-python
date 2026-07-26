"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MatchedDataBinding``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.data_binding_value


class MatchedDataBinding(TypedDict, closed=True):
    value: "capo_iotsitewise.types.data_binding_value.DataBindingValue"
    """<p>The value of the matched data binding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchedDataBinding) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.data_binding_value

    out["value"] = capo_iotsitewise.types.data_binding_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> MatchedDataBinding:
    out: MatchedDataBinding = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import capo_iotsitewise.types.data_binding_value

        out["value"] = capo_iotsitewise.types.data_binding_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("MatchedDataBinding.value required")
    return out
