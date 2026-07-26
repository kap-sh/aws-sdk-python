"""Generated from Smithy shape ``com.amazonaws.omics#FormatOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_omics.types.tsv_options
    import capo_omics.types.vcf_options


class _FormatOptions_tsvOptions(TypedDict, closed=True):
    tsvOptions: "capo_omics.types.tsv_options.TsvOptions"


class _FormatOptions_vcfOptions(TypedDict, closed=True):
    vcfOptions: "capo_omics.types.vcf_options.VcfOptions"


FormatOptions: TypeAlias = _FormatOptions_tsvOptions | _FormatOptions_vcfOptions


# --- restJson1 ser/de ---
def serialize_json(value: FormatOptions) -> dict:
    if "tsvOptions" in value:
        import capo_omics.types.tsv_options

        return {
            "tsvOptions": capo_omics.types.tsv_options.serialize_json(
                value["tsvOptions"]
            )
        }
    elif "vcfOptions" in value:
        import capo_omics.types.vcf_options

        return {
            "vcfOptions": capo_omics.types.vcf_options.serialize_json(
                value["vcfOptions"]
            )
        }
    else:
        raise SerializationError("FormatOptions: no variant present")


def deserialize_json(data: dict) -> FormatOptions:
    if "tsvOptions" in data:
        import capo_omics.types.tsv_options

        return {
            "tsvOptions": capo_omics.types.tsv_options.deserialize_json(
                data["tsvOptions"]
            )
        }
    elif "vcfOptions" in data:
        import capo_omics.types.vcf_options

        return {
            "vcfOptions": capo_omics.types.vcf_options.deserialize_json(
                data["vcfOptions"]
            )
        }
    else:
        raise DeserializationError("FormatOptions: no recognized variant key")
