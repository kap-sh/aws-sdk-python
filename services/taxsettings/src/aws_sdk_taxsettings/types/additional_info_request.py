"""Generated from Smithy shape ``com.amazonaws.taxsettings#AdditionalInfoRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.belgium_additional_info
    import aws_sdk_taxsettings.types.canada_additional_info
    import aws_sdk_taxsettings.types.chile_additional_info
    import aws_sdk_taxsettings.types.egypt_additional_info
    import aws_sdk_taxsettings.types.estonia_additional_info
    import aws_sdk_taxsettings.types.france_additional_info
    import aws_sdk_taxsettings.types.georgia_additional_info
    import aws_sdk_taxsettings.types.greece_additional_info
    import aws_sdk_taxsettings.types.indonesia_additional_info
    import aws_sdk_taxsettings.types.israel_additional_info
    import aws_sdk_taxsettings.types.italy_additional_info
    import aws_sdk_taxsettings.types.kenya_additional_info
    import aws_sdk_taxsettings.types.malaysia_additional_info
    import aws_sdk_taxsettings.types.philippines_additional_info
    import aws_sdk_taxsettings.types.poland_additional_info
    import aws_sdk_taxsettings.types.romania_additional_info
    import aws_sdk_taxsettings.types.saudi_arabia_additional_info
    import aws_sdk_taxsettings.types.south_korea_additional_info
    import aws_sdk_taxsettings.types.spain_additional_info
    import aws_sdk_taxsettings.types.turkey_additional_info
    import aws_sdk_taxsettings.types.ukraine_additional_info
    import aws_sdk_taxsettings.types.uzbekistan_additional_info
    import aws_sdk_taxsettings.types.vietnam_additional_info


class AdditionalInfoRequest(TypedDict):
    malaysia_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.malaysia_additional_info.MalaysiaAdditionalInfo"
    ]
    """<p> Additional tax information to specify for a TRN in Malaysia.</p>"""
    israel_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.israel_additional_info.IsraelAdditionalInfo"
    ]
    """<p> Additional tax information to specify for a TRN in Israel.</p>"""
    estonia_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.estonia_additional_info.EstoniaAdditionalInfo"
    ]
    """<p> Additional tax information to specify for a TRN in Estonia.</p>"""
    canada_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.canada_additional_info.CanadaAdditionalInfo"
    ]
    """<p> Additional tax information associated with your TRN in Canada.</p>"""
    spain_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.spain_additional_info.SpainAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in Spain.</p>"""
    kenya_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.kenya_additional_info.KenyaAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in Kenya.</p>"""
    south_korea_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.south_korea_additional_info.SouthKoreaAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in South Korea.</p>"""
    turkey_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.turkey_additional_info.TurkeyAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in Turkey.</p>"""
    georgia_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.georgia_additional_info.GeorgiaAdditionalInfo"
    ]
    """<p> Additional tax information to specify for a TRN in Georgia. </p>"""
    italy_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.italy_additional_info.ItalyAdditionalInfo"
    ]
    """<p> Additional tax information to specify for a TRN in Italy. </p>"""
    romania_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.romania_additional_info.RomaniaAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in Romania.</p>"""
    ukraine_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.ukraine_additional_info.UkraineAdditionalInfo"
    ]
    """<p> Additional tax information associated with your TRN in Ukraine. </p>"""
    poland_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.poland_additional_info.PolandAdditionalInfo"
    ]
    """<p> Additional tax information associated with your TRN in Poland. </p>"""
    saudi_arabia_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.saudi_arabia_additional_info.SaudiArabiaAdditionalInfo"
    ]
    """<p> Additional tax information associated with your TRN in Saudi Arabia. </p>"""
    indonesia_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.indonesia_additional_info.IndonesiaAdditionalInfo"
    ]
    """<p> </p>"""
    vietnam_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.vietnam_additional_info.VietnamAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in Vietnam. </p>"""
    egypt_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.egypt_additional_info.EgyptAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in Egypt. </p>"""
    greece_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.greece_additional_info.GreeceAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in Greece.</p>"""
    uzbekistan_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.uzbekistan_additional_info.UzbekistanAdditionalInfo"
    ]
    """<p> Additional tax information to specify for a TRN in Uzbekistan. </p>"""
    philippines_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.philippines_additional_info.PhilippinesAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in the Philippines.</p>"""
    belgium_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.belgium_additional_info.BelgiumAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in Belgium.</p>"""
    chile_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.chile_additional_info.ChileAdditionalInfo"
    ]
    """<p> Additional tax information to specify for a TRN in Chile.</p>"""
    france_additional_info: NotRequired[
        "aws_sdk_taxsettings.types.france_additional_info.FranceAdditionalInfo"
    ]
    """<p>Additional tax information to specify for a TRN in France.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalInfoRequest) -> dict:
    out: dict = {}
    if "malaysia_additional_info" in value:
        import aws_sdk_taxsettings.types.malaysia_additional_info

        out["malaysiaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.malaysia_additional_info.serialize_json(
                value["malaysia_additional_info"]
            )
        )
    if "israel_additional_info" in value:
        import aws_sdk_taxsettings.types.israel_additional_info

        out["israelAdditionalInfo"] = (
            aws_sdk_taxsettings.types.israel_additional_info.serialize_json(
                value["israel_additional_info"]
            )
        )
    if "estonia_additional_info" in value:
        import aws_sdk_taxsettings.types.estonia_additional_info

        out["estoniaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.estonia_additional_info.serialize_json(
                value["estonia_additional_info"]
            )
        )
    if "canada_additional_info" in value:
        import aws_sdk_taxsettings.types.canada_additional_info

        out["canadaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.canada_additional_info.serialize_json(
                value["canada_additional_info"]
            )
        )
    if "spain_additional_info" in value:
        import aws_sdk_taxsettings.types.spain_additional_info

        out["spainAdditionalInfo"] = (
            aws_sdk_taxsettings.types.spain_additional_info.serialize_json(
                value["spain_additional_info"]
            )
        )
    if "kenya_additional_info" in value:
        import aws_sdk_taxsettings.types.kenya_additional_info

        out["kenyaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.kenya_additional_info.serialize_json(
                value["kenya_additional_info"]
            )
        )
    if "south_korea_additional_info" in value:
        import aws_sdk_taxsettings.types.south_korea_additional_info

        out["southKoreaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.south_korea_additional_info.serialize_json(
                value["south_korea_additional_info"]
            )
        )
    if "turkey_additional_info" in value:
        import aws_sdk_taxsettings.types.turkey_additional_info

        out["turkeyAdditionalInfo"] = (
            aws_sdk_taxsettings.types.turkey_additional_info.serialize_json(
                value["turkey_additional_info"]
            )
        )
    if "georgia_additional_info" in value:
        import aws_sdk_taxsettings.types.georgia_additional_info

        out["georgiaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.georgia_additional_info.serialize_json(
                value["georgia_additional_info"]
            )
        )
    if "italy_additional_info" in value:
        import aws_sdk_taxsettings.types.italy_additional_info

        out["italyAdditionalInfo"] = (
            aws_sdk_taxsettings.types.italy_additional_info.serialize_json(
                value["italy_additional_info"]
            )
        )
    if "romania_additional_info" in value:
        import aws_sdk_taxsettings.types.romania_additional_info

        out["romaniaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.romania_additional_info.serialize_json(
                value["romania_additional_info"]
            )
        )
    if "ukraine_additional_info" in value:
        import aws_sdk_taxsettings.types.ukraine_additional_info

        out["ukraineAdditionalInfo"] = (
            aws_sdk_taxsettings.types.ukraine_additional_info.serialize_json(
                value["ukraine_additional_info"]
            )
        )
    if "poland_additional_info" in value:
        import aws_sdk_taxsettings.types.poland_additional_info

        out["polandAdditionalInfo"] = (
            aws_sdk_taxsettings.types.poland_additional_info.serialize_json(
                value["poland_additional_info"]
            )
        )
    if "saudi_arabia_additional_info" in value:
        import aws_sdk_taxsettings.types.saudi_arabia_additional_info

        out["saudiArabiaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.saudi_arabia_additional_info.serialize_json(
                value["saudi_arabia_additional_info"]
            )
        )
    if "indonesia_additional_info" in value:
        import aws_sdk_taxsettings.types.indonesia_additional_info

        out["indonesiaAdditionalInfo"] = (
            aws_sdk_taxsettings.types.indonesia_additional_info.serialize_json(
                value["indonesia_additional_info"]
            )
        )
    if "vietnam_additional_info" in value:
        import aws_sdk_taxsettings.types.vietnam_additional_info

        out["vietnamAdditionalInfo"] = (
            aws_sdk_taxsettings.types.vietnam_additional_info.serialize_json(
                value["vietnam_additional_info"]
            )
        )
    if "egypt_additional_info" in value:
        import aws_sdk_taxsettings.types.egypt_additional_info

        out["egyptAdditionalInfo"] = (
            aws_sdk_taxsettings.types.egypt_additional_info.serialize_json(
                value["egypt_additional_info"]
            )
        )
    if "greece_additional_info" in value:
        import aws_sdk_taxsettings.types.greece_additional_info

        out["greeceAdditionalInfo"] = (
            aws_sdk_taxsettings.types.greece_additional_info.serialize_json(
                value["greece_additional_info"]
            )
        )
    if "uzbekistan_additional_info" in value:
        import aws_sdk_taxsettings.types.uzbekistan_additional_info

        out["uzbekistanAdditionalInfo"] = (
            aws_sdk_taxsettings.types.uzbekistan_additional_info.serialize_json(
                value["uzbekistan_additional_info"]
            )
        )
    if "philippines_additional_info" in value:
        import aws_sdk_taxsettings.types.philippines_additional_info

        out["philippinesAdditionalInfo"] = (
            aws_sdk_taxsettings.types.philippines_additional_info.serialize_json(
                value["philippines_additional_info"]
            )
        )
    if "belgium_additional_info" in value:
        import aws_sdk_taxsettings.types.belgium_additional_info

        out["belgiumAdditionalInfo"] = (
            aws_sdk_taxsettings.types.belgium_additional_info.serialize_json(
                value["belgium_additional_info"]
            )
        )
    if "chile_additional_info" in value:
        import aws_sdk_taxsettings.types.chile_additional_info

        out["chileAdditionalInfo"] = (
            aws_sdk_taxsettings.types.chile_additional_info.serialize_json(
                value["chile_additional_info"]
            )
        )
    if "france_additional_info" in value:
        import aws_sdk_taxsettings.types.france_additional_info

        out["franceAdditionalInfo"] = (
            aws_sdk_taxsettings.types.france_additional_info.serialize_json(
                value["france_additional_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdditionalInfoRequest:
    out: AdditionalInfoRequest = {}  # type: ignore[typeddict-item]
    if "malaysiaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.malaysia_additional_info

        out["malaysia_additional_info"] = (
            aws_sdk_taxsettings.types.malaysia_additional_info.deserialize_json(
                data["malaysiaAdditionalInfo"]
            )
        )
    if "israelAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.israel_additional_info

        out["israel_additional_info"] = (
            aws_sdk_taxsettings.types.israel_additional_info.deserialize_json(
                data["israelAdditionalInfo"]
            )
        )
    if "estoniaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.estonia_additional_info

        out["estonia_additional_info"] = (
            aws_sdk_taxsettings.types.estonia_additional_info.deserialize_json(
                data["estoniaAdditionalInfo"]
            )
        )
    if "canadaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.canada_additional_info

        out["canada_additional_info"] = (
            aws_sdk_taxsettings.types.canada_additional_info.deserialize_json(
                data["canadaAdditionalInfo"]
            )
        )
    if "spainAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.spain_additional_info

        out["spain_additional_info"] = (
            aws_sdk_taxsettings.types.spain_additional_info.deserialize_json(
                data["spainAdditionalInfo"]
            )
        )
    if "kenyaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.kenya_additional_info

        out["kenya_additional_info"] = (
            aws_sdk_taxsettings.types.kenya_additional_info.deserialize_json(
                data["kenyaAdditionalInfo"]
            )
        )
    if "southKoreaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.south_korea_additional_info

        out["south_korea_additional_info"] = (
            aws_sdk_taxsettings.types.south_korea_additional_info.deserialize_json(
                data["southKoreaAdditionalInfo"]
            )
        )
    if "turkeyAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.turkey_additional_info

        out["turkey_additional_info"] = (
            aws_sdk_taxsettings.types.turkey_additional_info.deserialize_json(
                data["turkeyAdditionalInfo"]
            )
        )
    if "georgiaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.georgia_additional_info

        out["georgia_additional_info"] = (
            aws_sdk_taxsettings.types.georgia_additional_info.deserialize_json(
                data["georgiaAdditionalInfo"]
            )
        )
    if "italyAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.italy_additional_info

        out["italy_additional_info"] = (
            aws_sdk_taxsettings.types.italy_additional_info.deserialize_json(
                data["italyAdditionalInfo"]
            )
        )
    if "romaniaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.romania_additional_info

        out["romania_additional_info"] = (
            aws_sdk_taxsettings.types.romania_additional_info.deserialize_json(
                data["romaniaAdditionalInfo"]
            )
        )
    if "ukraineAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.ukraine_additional_info

        out["ukraine_additional_info"] = (
            aws_sdk_taxsettings.types.ukraine_additional_info.deserialize_json(
                data["ukraineAdditionalInfo"]
            )
        )
    if "polandAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.poland_additional_info

        out["poland_additional_info"] = (
            aws_sdk_taxsettings.types.poland_additional_info.deserialize_json(
                data["polandAdditionalInfo"]
            )
        )
    if "saudiArabiaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.saudi_arabia_additional_info

        out["saudi_arabia_additional_info"] = (
            aws_sdk_taxsettings.types.saudi_arabia_additional_info.deserialize_json(
                data["saudiArabiaAdditionalInfo"]
            )
        )
    if "indonesiaAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.indonesia_additional_info

        out["indonesia_additional_info"] = (
            aws_sdk_taxsettings.types.indonesia_additional_info.deserialize_json(
                data["indonesiaAdditionalInfo"]
            )
        )
    if "vietnamAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.vietnam_additional_info

        out["vietnam_additional_info"] = (
            aws_sdk_taxsettings.types.vietnam_additional_info.deserialize_json(
                data["vietnamAdditionalInfo"]
            )
        )
    if "egyptAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.egypt_additional_info

        out["egypt_additional_info"] = (
            aws_sdk_taxsettings.types.egypt_additional_info.deserialize_json(
                data["egyptAdditionalInfo"]
            )
        )
    if "greeceAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.greece_additional_info

        out["greece_additional_info"] = (
            aws_sdk_taxsettings.types.greece_additional_info.deserialize_json(
                data["greeceAdditionalInfo"]
            )
        )
    if "uzbekistanAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.uzbekistan_additional_info

        out["uzbekistan_additional_info"] = (
            aws_sdk_taxsettings.types.uzbekistan_additional_info.deserialize_json(
                data["uzbekistanAdditionalInfo"]
            )
        )
    if "philippinesAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.philippines_additional_info

        out["philippines_additional_info"] = (
            aws_sdk_taxsettings.types.philippines_additional_info.deserialize_json(
                data["philippinesAdditionalInfo"]
            )
        )
    if "belgiumAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.belgium_additional_info

        out["belgium_additional_info"] = (
            aws_sdk_taxsettings.types.belgium_additional_info.deserialize_json(
                data["belgiumAdditionalInfo"]
            )
        )
    if "chileAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.chile_additional_info

        out["chile_additional_info"] = (
            aws_sdk_taxsettings.types.chile_additional_info.deserialize_json(
                data["chileAdditionalInfo"]
            )
        )
    if "franceAdditionalInfo" in data:
        import aws_sdk_taxsettings.types.france_additional_info

        out["france_additional_info"] = (
            aws_sdk_taxsettings.types.france_additional_info.deserialize_json(
                data["franceAdditionalInfo"]
            )
        )
    return out
